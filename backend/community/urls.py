from django.urls import path
from . import views


urlpatterns = [
  path('', views.Boards.as_view()), 
  path('<int:board_pk>/', views.BoardDetail.as_view()),
  path('<int:board_pk>/favorite/', views.favorite), 
  path('<int:board_pk>/article/', views.Articles.as_view()),
  path('<int:board_pk>/<int:article_pk>/', views.ArticleDetail.as_view()),
  path('<int:board_pk>/<int:article_pk>/like/', views.like_article),
  path('<int:board_pk>/<int:article_pk>/<int:comment_pk>/', views.CommentDetail.as_view()),
]