# 어린이ZIP

> 특화-Sub PJT 3
>
> 2020.09.21~2020.10.08(총 3주)

| 이름         | 역할                                   |
| ------------ | -------------------------------------- |
| 김명석(팀장) | Frontend Develop                       |
| 서용준       | Backend Develop                        |
| 서지훈       | Frontend Develop                       |
| 안성민       | Fullstack Develop, 데이터 수집 및 정제 |
| 허예슬       | Backend Develop                        |

<br><br>

![Github](https://img.shields.io/badge/vue-2.6.11-%234FC08D?style=plastic&logo=Vue.js)![Github](https://img.shields.io/pypi/djversions/djangorestframework?color=green&label=django&logo=django&style=plastic)![Github](https://img.shields.io/badge/MySQL-8.0-%234479A1?style=plastic&logo=mysql)![Github](https://img.shields.io/badge/build-passing-brightgreen?style=plastic)

<br>



### 사용된 기술

<img src="./img/skill_set.png" width=100%>



### 프로젝트 구조(한)

```
.
├── .gitignore # Git 버전 관리에서 제외할 파일 목록을 지정하는 파일
├── README.md
├── img # 이미지 관련 폴더
├── members_docs # 팀원 문서화
├── frontend
│   ├── assets # style, image, font 등 컴파일 되지 않는 리소스 관련 폴더
│   ├── pages # 응용프로그램 보기 및 경로(라우팅)을 포함
│   │   ├── board # 게시판 관련 페이지
│   │   ├── community # 커뮤니티 관련 페이지
│   │   ├── kinder # 어린이집 관련 페이지
│   │   ├── signup # 계정관련 페이지
│   │   └── ... # 라우팅 될 각 페이지
│   ├── static # 변경되지 않는 정적 파일(favicon, robots.txt, sitemap.xml 등)
│   ├── nuxt.config.js # Nuxt.js 에 대한 config 파일
│   ├── package.json # Vue에서 사용하는 것과 동일하게 종속성 및 스크립트 작성
│   ├── layouts # 각 page에 고정된 레이아웃을 반복해서 설정해서 넣어줘야 할경우
│   └── components # Nuxt.js가 스캔해서 자동으로 가져옴
│       ├── Common # 헤더, 푸터, 공통 컴포넌트 관련
│       ├── Community # 커뮤니티 관련
│       ├── Home # 메인페이지 관련
│       ├── Kinder # 어린이집 관련
│       ├── Launcher # 런처페이지
│       └── Search # 검색 관련
└── backend
    ├── account # 계정 API
    ├── community # 게시판 API
    ├── kindergartens # 어린이집 API
    ├── spc_pjt # Django 설정 파일
    ├── templates
    ├── Dockerfile # Django 이미지 작업
    ├── manage.py # Django 실행 파일
    ├── requirements.txt # 의존성 관리
    └── bigdata
        ├── analyze.py # 크롤링해온 어린이집 정보 정형화 및 저장
    	├── crawling.py # 어린이집 정보 크롤링 할 코드
    	├── recommend.py # 추천알고리즘을 적용 할 코드
    	└── requriements.txt # 의존성 관리
    	
```

### 프로젝트 구조(영)

```
.
├── .gitignore # Files that specify a list of files to exclude from Git version management
├── README.md
├── img # Related images folder
├── members_docs # Documentation for team members
├── frontend
│   ├── assets # Uncomplied resource related folders such as style, image, and font
│   ├── pages # Includes application views and paths(routing)
│   │   ├── board # Related board pages
│   │   ├── community # Related community pages
│   │   ├── kinder # Related children and kindergarten pages
│   │   ├── signup # Related account pages
│   │   └── ... # Each page to be routed
│   ├── static # Static files do not change(favicon, robots.txt, sitemap.xml etc.)
│   ├── nuxt.config.js # config file for nuxt.js
│   ├── package.json # Dependencies and scripting
│   ├── layouts # Need to repeat the fixed layout on each page and put it in.
│   └── components # Nust.js scanned and automatically imported
│       ├── Common # Related Header, Footer, Common commponents UI
│       ├── Community # Related community UI
│       ├── Home # Related main UI
│       ├── Kinder # Related children, kindergarten UI
│       ├── Launcher # 런처페이지 Related launcher UI
│       └── Search # 검색 관련 Related search UI
└── backend
    ├── account # Account API
    ├── community # Board API
    ├── kindergartens # Kindergarten API
    ├── spc_pjt # Django setup file
    ├── templates
    ├── Dockerfile # Image file for containerizing Django
    ├── manage.py # Django run file
    ├── requirements.txt # dependency management
    └── bigdata
        ├── analyze.py # Formatting and saving infomation on the crawling kindergarten data
    	├── crawling.py # Code for crawling kindergarten data
    	├── recommend.py # Code for applying recommended algorithm
    	└── requriements.txt # dependency management
```



### 프로젝트 프로세스

<img src="./img/process_struct.png" width=100%>



### 서비스 개요 

`어린이zip`은 어린이집 데이터를 기반으로 사용자의 니즈와 기호를 반영해 어린이집을 추천해주는 웹 애플리케이션(web application)입니다. 



### 개발 동기

> 어린 자녀를 둔 부모님과의 인터뷰를 통해 어린이집을 선택할 때 일반적으로 지인의 추천 혹은 네이버 카페 등을 이용해 정보를 탐색하지만 그 과정에서 많은 정보가 퍼져있어 곤혹을 겪는다는 사실을 알게되었습니다. 
>
> 어린이집 정보를 한 눈에 볼 수 있고, 또 자녀에게 꼭 맞는 어린이집을 추천해줌으로써 부모님들이 어린이집을 탐색할 때 느끼는 피곤함을 덜 수 있지 않을까? 라는 생각으로 프로젝트를 기획하였습니다. 
>



### 주요 기능

- 전국 어린이집 조회 
  - 필터 기능 
  - 어린이집 찜 기능
- 어린이집 추천
  - 사용자가 입력 및 클릭한 데이터를 바탕으로 비슷한 어린이집 추천 
- 커뮤니티
  - 원하는 게시판 생성 기능
  - 게시판 즐겨찾기  
- 원장과 원격 화상 상담 



- 어린이집 정보와 더불어 지역구별 인구당 범죄 발생 빈도 & 강력 범죄 비율 시각화
- 어린이집 리뷰 데이터를 기반으로 어린이집 추천 

<br><br>
[<img src="./img/logo.png" width=50>](http://childrenzip.site/)를 클릭해 사이트를 확인하세요! 😊

### 사용 기술

```
DB : MySQL
Language : Python, JavaScript
Browser : Chrome
FrameWork : Django, Vue, Nuxt
ETC : Docker
```



### ERD

[ERD Diagram](https://www.erdcloud.com/d/a36xRNx6woXE7ukPk)

<br><br>