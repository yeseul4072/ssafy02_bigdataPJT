from django.db import models
from django.conf import settings

# Create your models here.
class Board(models.Model):
  title = models.CharField(max_length=50)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  # favorite_user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Favorite', related_name='favorite_board')


class Favorite(models.Model):
  created_at = models.DateField(auto_now_add=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  board = models.ForeignKey(Board, on_delete=models.CASCADE)


class Article(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  board = models.ForeignKey(Board, on_delete=models.CASCADE)
  like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_article')


class Comment(models.Model):
  content = models.TextField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
