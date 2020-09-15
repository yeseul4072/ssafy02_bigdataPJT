from drf_yasg import openapi
from rest_framework import serializers
from .models import Board, Article, Comment

header = openapi.Parameter(
    'Authorization',
    openapi.IN_HEADER,
    description='"Token {키값}"의 형태로 토큰을 입력하세요.',
    type=openapi.TYPE_STRING
)

class BoardCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title']

class ArticleCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content']

class CommentCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']