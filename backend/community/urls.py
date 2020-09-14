from django.urls import path
from . import views


urlpatterns = [
  path('board/', views.Boards.as_view()),
  path('board/<int:board_pk>/', views.BoardDetail.as_view()),
  path('board/<int:board_pk>/article/', views.Articles.as_view()),
]