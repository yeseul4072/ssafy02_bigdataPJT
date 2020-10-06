from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from allauth.account.views import confirm_email
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings  
from django.conf.urls.static import static  


schema_view = get_schema_view(
    openapi.Info(
        title='어린이ZIP API',
        default_version='v1',
        description='어린이ZIP API입니다',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='myemail@gmail.com'), # 나중에 서비스 email만들어서 등록하면 좋을듯
        license=openapi.License(name="children-zip's License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')), # rest_auth url 등록
    path('rest-auth/', include('accounts.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')), # 회원가입
    path('accounts/', include('allauth.urls')), # 회원가입 email
    path('accounts-rest/registration/account-confirm-email/<str:key>/', confirm_email, name='account_confirm_email'), # 회원가입 email verification
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # swagger
    path('community/', include('community.urls')),
    path('kindergartens/', include('kindergartens.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
