### Interface

```
.
ㄴ back-end   (백 폴더)
ㄴ front-end  (프론트 폴더)
ㄴ bigdata    (데이터 폴더)
ㄴ README.md  

추후
ㄴ images (이미지 관련 -> readme.md에 들어갈 폴더)
```

.

## **가상환경 설정 및 django 프로젝트 생성 (REST API)**

### **1. 가상환경 생성 및 실행**

### **a. 가상환경 만들기**

- 프로젝트를 여러 개 진행하면 각각의 프로젝트에서 사용하는 패키지들끼리 충돌이 날 수 있다.

  - 프로젝트 마다 독립적인 환경을 만들어준다.

- 원하는 폴더에서 다음 명령어를 실행한다.

  ```
  python -m venv venv
  ```

  - venv(뒤에 있는 venv)라는 이름으로 가상환경(virtualenv)를 생성한다

### **b. 가상환경 실행**

- 가상환경 폴더(venv)가 만들어진 디렉토리에서 다음 명령어를 실행한다.

  ```
  source venv/Scripts/activate
  # 윈도우 환경
  source venv/bin/activate
  # 리눅스 환경
  ```

- 가상환경 폴더를 생성하고 난 후에는 `.gitignore`를 사용하여 `venv` 폴더가 푸시되지 않도록 하는 게 좋다.

- `pip list` 명령어를 통해 가상환경에 설치된 패키지 리스트를 보면 다음과 같이 나온다.

  ```
  $ pip list
  Package    Version
  ---------- -------
  pip        19.2.3
  setuptools 41.2.0
  ```

### **2. django 프로젝트 생성**

### **a. django 설치하기**

- ```
  pip install django
  ```

   명령어로 설치할 수 있다.

  - `pip install django==2.1.15`와 같이 설치할 때 버전을 명시할 수 있다.

### **b. django 프로젝트 생성**

- `django-admin startproject {프로젝트 이름}` 명령어로 django 프로젝트를 만들 수 있다.

  - ```
    django-admin startproject {프로젝트 이름} .
    ```

    과 같이 

    ```
    .
    ```

    을 붙여주면 현재 폴더에 django 프로젝트를 만들 수 있다.

    - 즉, 현재 폴더에 `manage.py` 파일이 생긴다.

- `manage.py`가 있는 디렉토리에서 `python manage.py runserver` 명령어를 통해 서버가 실행되는 것을 볼 수 있다.

- django 프로젝트 첫 화면

  ![https://i.ibb.co/yQV6DTq/djangomain.jpg](https://i.ibb.co/yQV6DTq/djangomain.jpg)

### **c. django rest framework 설치**

1. `pip install djangorestframework` 명령어를 통해 django rest framework를 설치한다.

   - django REST API를 만들기 위한 프레임워크이다.

2. `settings.py`의 `INSTALLED_APPS` 변수에 `'rest_framework'`를 추가한다.

   ```python
   # settings.py
   
   INSTALLED_APPS = [
       # default
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   
       # DRF
       'rest_framework'
   ]
   ```



## 요청과 응답

### 요청(request)객체

```python
request.POST # 폼 데이터만 다루며, POST 메서드에서만 사용 가능
request.data # 아무 데이터나 다룰 수 있고, POST뿐만 아니라, PUT, PATCH에서도 이용 가능
```

### 상태코드

DRF는 `status` 객체를 제공한다

```python
return Response(status=status.HTTP_204_NO_CONTENT)
```

## Serializer

github에서 `Serializer` 코드를 살펴보자.

```python
# rest_framework/serializers.py

class BaseSerializer(Field):
    def __init__(self, instance=None, data=empty, **kwargs):
        # 생략
        
class Serializer(BaseSeializer):
  # 생략
```

`Serializer` 는 `BaseSerializer` 를 상속 받고있다.

따라서 instance가 먼저 나온다면 뒤에 data라는 keyword를 써줄 필요가 없지만, instance 없이 data를 파라미터로 넘기기 위해서는 keyword가 꼭 필요하다.

```python
serializer = PostSerializer(post)
serializer = PostSerializer(data=request.data)
serializer = PostSerializer(post, data=request.data)
serializer = PostSerializer(post, request.data)
serializer = PostSerializer(request.data) # 오류!
```

data에 파라미터가 주어지면 다음과 같은 과정을 거친다.

1. serizlizer.is_valid() : data의 유효성 검사
2. serializer.save() : 유효한 데이터 저장
3. serializer.errors : 유효성 검사에서의 오류 저장
4. serializer.data : 유효성 검사 후 인스턴스 값이 딕셔너리로 저장

### serializer.save()

```python
def save(self, **kwargs):
  pass
```

serializer.save() 는 다음과 같이 **kwargs 를 받는다.





> DRF API 문서를 자동으로 만들어주는 패키지

### 설치

```python
pip install -U drf-yasg
```

### 시작하기

```python
# settings.py

INSTALLED_APPS = [
   ...
   'drf_yasg',
   ...
]
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_url_v1_patterns = [
    path('v1/', include('musics.urls')),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="<https://www.google.com/policies/terms/>",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex'],
   public=True,
   permission_classes=(permissions.AllowAny,),
   patterns=schema_url_v1_patterns,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('musics.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

### API 설명 커스터마이징

```python
#views.py

...
@api_view(['GET'])
def music_list(request):
  """
  음악 리스트를 저장하거나 불러오는 API

  ---
  # 내용
    - id: pk
    - title : 음악 제목
    - artist_id : 작곡가 id
  """
  musics = Music.objects.all()
  serializer = MusicSerializer(musics, many=True)
  return Response(serializer.data)
```

- 타이틀을 쓰고 엔터를 한 다음 `---`을 써줘야 제대로 커스터마이징된다.