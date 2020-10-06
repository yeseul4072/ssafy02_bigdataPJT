from django.urls import path
from . import views


urlpatterns = [
  path('delete/', views.user_delete, name='user_delete'), 
  path('user/profile/', views.user_profile, name='user_profile'),
  path('user/update/', views.user_update, name='user_update'),
  # path('kakao/login/', views.kakao_login, name='kakao_login'),
  # path('kakao/login/callback/', views.kakao_callback, name='kakao_callback'),
]