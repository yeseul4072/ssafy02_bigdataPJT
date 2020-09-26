from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.Recommend.as_view()),
]