from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import News
from django.conf import settings
import requests
import xml.etree.ElementTree as ET # xml 형식을 처리하는 라이브러리
from typing import List
from konlpy.tag import Okt
from textrankr import TextRank

class OktTonkenizer:
    okt: Okt = Okt()
    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.phrases(text)
        return tokens
    
def index(request):
    news_list = News.objects.order_by('-create_date')
    context = {'news_list' : news_list}
    return render(request, 'pybo/news_list.html',context)

def detail(request, news_id):
    news = get_object_or_404(News, pk = news_id)
    context = {'news': news}
    return render(request, 'pybo/news_detail.html', context)

def search(request):
    query = request.GET.get('kw')
    print('query:', query)
    if query:
        api_key = ''
        response = requests.get(f'https://stdict.korean.go.kr/api/search.do?certkey_no=6592&key={api_key}&type_search=search&req_type=json&q={query}')
        if response.status_code == 200:
            data = response.json()
            means_lst = []
            for i in data['channel']['item']:
                means_lst.append(i['sense']['definition'])
            # print(data['channel']['item'][0]['sense']['definition']) # 실제로 쓰일 데이터
            print(means_lst)
            meaning = means_lst
        else:
            meaning = '뜻을 찾을 수 없습니다.'
    else:
        meaning = '검색어를 입력하세요.'

    return JsonResponse({'meaning': meaning})

def summary(request, content, news_id):
    news = News.objects.get(id=news_id)
    if news.summary:
        summaries = news.summary
        summaries = summaries.split(',')
        summaries[0] = summaries[0][1:] # 괄호 제거
        summaries[2] = summaries[2][:-1]
    else:
        mytokenizer: OktTonkenizer = OktTonkenizer()
        textrank: TextRank = TextRank(mytokenizer)
        k: int = 3
        summaries: List[str] = textrank.summarize(content, k, verbose=False)
        # for summary in summaries:
        #     print(summary)
        news.summary = summaries
        news.save()
    return render(request, 'summary_news.html', {'content': summaries})

    
#추가
# def search(request):
#     query = request.GET.get('q')
#     if query:
#         response = requests.get('https://newsapi.org/v2/everything', params={'q': query, 'apiKey': settings.NEWS_API_KEY})
#         articles = response.json().get('articles', [])
#         for article in articles:
#             News.objects.get_or_create(
#                 title=article['title'],
#                 content=article['content'],
#                 publication_date=article['publishedAt'][:10],
#                 summary=article['description'],
#                 summary_link=article['url']
#             )
#         articles = News.objects.filter(title__icontains=query)
#         return render(request, 'news/search_results.html', {'articles': articles, 'query': query})
#     return render(request, 'news/search_results.html')