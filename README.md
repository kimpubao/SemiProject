# 📰 뉴스 기사 요약 웹 애플리케이션

## 📌 프로젝트 개요

이 프로젝트는 Python의 Django 프레임워크와 자연어 처리 라이브러리인 `konlpy`를 활용하여 **뉴스 기사를 요약하는 웹 애플리케이션**을 개발하는 것입니다. 사용자가 설정한 키워드에 따라 관련성이 높은 기사를 탐색하고, 해당 기사의 내용을 요약하여 제공하는 기능을 구현하였습니다.

---

## 🛠 사용 기술 및 환경

- **언어**: <img src="https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python&logoColor=white"/>
- **프레임워크** <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>
- **자연어 처리** <img src="https://img.shields.io/badge/Konlpy-FF6600?style=flat-square&logo=python&logoColor=white" alt="Konlpy"/>
- **데이터베이스** <img src="https://img.shields.io/badge/Konlpy-FF6600?style=flat-square&logo=python&logoColor=white" alt="Konlpy"/>
- **기타**   <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>

---

## 🔍 주요 기능

1. **웹 페이지 개발**: Django를 이용하여 사용자 인터페이스를 구성하고, 뉴스 기사를 입력받는 폼을 구현하였습니다.
2. **뉴스 기사 스크래핑**: API를 활용하여 실시간으로 뉴스 기사를 수집하였습니다.
3. **자연어 처리 기반 요약**: `konlpy`를 활용하여 수집한 뉴스 기사의 핵심 내용을 추출하고 요약하였습니다.
4. **키워드 기반 검색**: 사용자가 입력한 키워드를 기반으로 관련성이 높은 기사를 탐색하였습니다.

---

## 📁 프로젝트 구조

- `manage.py`: Django 프로젝트 관리 스크립트
- `config/`: Django 프로젝트 설정 파일
- `pybo/`: 주요 애플리케이션 로직
- `templates/`: HTML 템플릿 파일
- `static/`: 정적 파일 (CSS, JS 등)
- `db.sqlite3`: SQLite 데이터베이스 파일
- `news.ipynb`, `news2.ipynb`: 뉴스 기사 수집 및 요약 관련 Jupyter 노트북

---

## 🧠 배운 점

- Django 프레임워크를 활용한 웹 애플리케이션 개발 과정을 익혔습니다.
- `konlpy`를 활용하여 한국어 자연어 처리 및 텍스트 요약 기법을 학습하였습니다.
- API를 통한 데이터 수집 및 처리 과정을 경험하였습니다.
- 키워드 기반의 정보 검색 및 관련성 분석 방법을 이해하였습니다.

---

## 🚀 향후 개선 사항

- 다양한 뉴스 소스를 추가하여 데이터의 다양성 확보
- 요약 알고리즘의 고도화를 통한 정확도 향상
- 사용자 맞춤형 뉴스 추천 기능 구현
- 반응형 웹 디자인을 통한 사용자 경험 개선

---

## 👥 팀원

- 최동현
- 김상준
- 안성진

---

## 📅 개발 기간

2024년 5월 13일 ~ 2024년 5월 20일
