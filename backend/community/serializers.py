from rest_framework import serializers
from .models import Board, Favorite, Article, Comment


class BoardSerializer(serializers.ModelSerializer):
  user = serializers.IntegerField(source='user.id', required=False)
  class Meta:
    model = Board
    fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
  user = serializers.IntegerField(source='user.id', required=False)
  board = serializers.IntegerField(source='user.id', required=False)
  class Meta:
    model = Article
    fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'board', 'user']


class ArticleCreateSerializer(serializers.ModelSerializer):
  user = serializers.IntegerField(source='user.id', required=False)
  board = serializers.IntegerField(source='user.id', required=False)
  class Meta:
    model = Article
    fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
  user = serializers.IntegerField(source='user.id', required=False)
  class Meta:
    model = Board
    fields = '__all__'
