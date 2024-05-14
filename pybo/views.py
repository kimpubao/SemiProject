from django.shortcuts import render, get_object_or_404
from .models import News
from django.conf import settings
import requests

def index(request):
    news_list = News.objects.order_by('-create_date')
    context = {'news_list' : news_list}
    return render(request, 'pybo/news_list.html',context)

def detail(request, news_id):
    news = get_object_or_404(News, pk = news_id)
    context = {'news': news}
    return render(request, 'pybo/news_detail.html', context)

#추가
def search(request):
    query = request.GET.get('q')
    if query:
        response = requests.get('https://newsapi.org/v2/everything', params={'q': query, 'apiKey': settings.NEWS_API_KEY})
        articles = response.json().get('articles', [])
        for article in articles:
            News.objects.get_or_create(
                title=article['title'],
                content=article['content'],
                publication_date=article['publishedAt'][:10],
                summary=article['description'],
                summary_link=article['url']
            )
        articles = News.objects.filter(title__icontains=query)
        return render(request, 'news/search_results.html', {'articles': articles, 'query': query})
    return render(request, 'news/search_results.html')