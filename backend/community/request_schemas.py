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

board_title = openapi.Parameter(
    'title',
    openapi.IN_QUERY,
    description='게시판 제목 (안 넣어도 됨)',
    type=openapi.TYPE_STRING
)

board_content = openapi.Parameter(
    'content',
    openapi.IN_QUERY,
    description='게시판 설명 (안 넣어도 됨)',
    type=openapi.TYPE_STRING
)

board_page = openapi.Parameter(
    'page',
    openapi.IN_QUERY,
    description='게시판 페이지 (게시판 10개씩, 안 넣으면 첫 번째 페이지)',
    type=openapi.TYPE_NUMBER
)

article_user = openapi.Parameter(
    'user',
    openapi.IN_QUERY,
    description='게시글 글쓴이 닉네임 (안 넣어도 됨)',
    type=openapi.TYPE_STRING
)

article_title = openapi.Parameter(
    'title',
    openapi.IN_QUERY,
    description='게시글 제목 (안 넣어도 됨)',
    type=openapi.TYPE_STRING
)

article_content = openapi.Parameter(
    'content',
    openapi.IN_QUERY,
    description='게시글 내용 (안 넣어도 됨)',
    type=openapi.TYPE_STRING
)

article_page = openapi.Parameter(
    'page',
    openapi.IN_QUERY,
    description='게시글 페이지 (게시판 10개씩, 안 넣으면 첫 번째 페이지)',
    type=openapi.TYPE_NUMBER
)

article_order = openapi.Parameter(
    'order',
    openapi.IN_QUERY,
    description='게시글 정렬 (기본(안 넣으면)-최신순 / 댓글 많은 순(order=comments) / 좋아요 많은 순(order=likes))',
    type=openapi.TYPE_STRING
)