from django.urls import path
from . import views


urlpatterns = [
  path('delete/', views.user_delete, name='user_delete'), 
  path('user/profile/', views.user_profile, name='user_profile'),
  path('user/update/', views.user_update, name='user_update'),
  path('validate/password/', views.password_validate, name='password_validate'),
  path('validate/username/', views.username_validate, name='username_validate'),
  path('validate/nickname/', views.nickname_validate, name='nickname_validate'),
  path('validate/email/', views.email_validate, name='email_validate'),
  # path('kakao/login/', views.kakao_login, name='kakao_login'),
  # path('kakao/login/callback/', views.kakao_callback, name='kakao_callback'),
]