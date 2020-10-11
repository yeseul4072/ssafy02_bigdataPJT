<img src="../img/banner.JPG" width=100%>

![Github](https://img.shields.io/badge/vue-2.6.11-%234FC08D?style=plastic&logo=Vue.js)![Github](https://img.shields.io/pypi/djversions/djangorestframework?color=green&label=django&logo=django&style=plastic)![Github](https://img.shields.io/badge/MySQL-8.0-%234479A1?style=plastic&logo=mysql)![Github](https://img.shields.io/badge/build-passing-brightgreen?style=plastic)



## 🏠 Daycare center recommendation platform, Children-ZIP

`Children-ZIP` is a web application that recommends a daycare center suitable for users.

Based on the user's location and activity within the website

It recommends daycare centers in a way that combines Content-Based Filtering and User-Based Collaborative Filtering techniques.

Click [here](http://childrenzip.site/) to check the site 🙂



## 📌 Table of Contents

- [Tech Stacks](#-Tech-Stacks)
- [Project Structure](#-Project-Structure)
- [ERD](#-ERD)
- [Project Process](#-Project-Process)
- [Main Function](#-Main-Function)
- [Demonstration](#-Demonstration)
- [Browsers Supported](#-Browsers-Supported)
- [Creator](#-Creator)
- [License](#-License)
- [Reference](#-Reference)



## 🔨 Tech Stacks

<img src="../img/skill_set.png" width=100%>



## 🧱 Project Structure

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



## 🔍 Project Process

<img src="../img/process_struct.png" width=100%>



## :globe_with_meridians: Browsers Supported

| <img src='../img/chrome.png' width=60> | <img src='../img/firefox.png' width=60> | <img src='../img/edge.png' width=60> | <img src='../img/safari.png' width=60> |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                            latest                            |                            latest                            |                            latest                            |                            latest                            |