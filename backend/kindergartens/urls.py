from django.urls import path
from . import views

urlpatterns = [
    path('counts/', views.Count),
    # main page
    path('feature-based-recommend/', views.FBasedRecommend.as_view()),
    path('activated-reviews/', views.ReviewActivated.as_view()),
    # kidergarten detail page
    path('<int:kindergarten_pk>/', views.KindergartenDetail.as_view()),
    path('<int:kindergarten_pk>/reviews/', views.Reviews.as_view()),
    path('<int:kindergarten_pk>/review/<int:review_pk>/', views.ReviewDetail.as_view()),
    # kindergarten list page
    path('', views.Kindergartens.as_view()),
    # 찜
    path('wishlist/<int:kindergarten_pk>/', views.WishList),
    # 리뷰 좋아요
    path('review/<int:review_pk>/like/', views.like_review),
    # 군/구
    path('boroughs/', views.boroughs),
    # 동
    path('boroughs/<int:borough_pk>/', views.villages),
    # kindergarten image
    path('image/<int:kindergarten_pk>/', views.kindergarten_image),
]