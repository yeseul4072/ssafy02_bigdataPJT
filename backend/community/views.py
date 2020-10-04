# django
from django.shortcuts import get_object_or_404
from django.db.models import Count

# DRF
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

# swagger
from drf_yasg.utils import swagger_auto_schema
from . import request_schemas

# App - community
from .models import Board, Favorite, Article, Comment
from .serializers import (BoardSerializer, BoardListSerializer, BoardDetailSerializer, ArticleSerializer, 
ArticleCreateSerializer, ArticleDetailSerializer,CommentCreateSerializer, ArticleCommentSerializer)


class Pagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    max_page_size = 100


class Boards(APIView):
    pagination_class = Pagination
    serializer_class = BoardListSerializer
    
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                   self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
    
    @swagger_auto_schema(responses={200: BoardSerializer})
    def get(self, request):
        """
        게시판 목록 조회

        ## 게시판 목록 조회
        - 게시판 list를 불러옵니다.
        - params로 page, title, content를 보냅니다. 
        """
        title = request.GET.get('title', None)
        content = request.GET.get('content', None)
        if title:
            instance = Board.objects.filter(title__contains=title)
        elif content:
            instance = Board.objects.filter(content__contains=content)
        else:
            instance = Board.objects.all()
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, context={'request': request}, many=True).data)
        else:
            serializer = self.serializer_class(instance, context={'request': request}, many=True)
        return Response(serializer.data)

    
    # 게시판 create - params : title
    @swagger_auto_schema(
        request_body=request_schemas.BoardCreateRequest,
        manual_parameters=[request_schemas.header],
        responses={
            201: BoardSerializer
        }
    )
    def post(self, request):
        """
        게시판 생성

        ## 게시판 생성
        - title을 받아 게시판을 생성합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        """
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDetail(APIView):
    def get(self, request, board_pk):
        """
        게시판 조회

        ## 게시판 조회
        - 해당 게시판의 자세한 정보를 조회
        """
        board = Board.objects.get(pk=board_pk)
        serializer = BoardDetailSerializer(board, context={'request': request})
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=request_schemas.BoardCreateRequest,
        manual_parameters=[request_schemas.header],
        responses={
            200: BoardSerializer
        }
    )
    def put(self, request, board_pk):
        """
        게시판 수정

        ## 게시판 수정
        - 게시판 제목을 수정할 수 있습니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        """
        board = Board.objects.get(pk=board_pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(manual_parameters=[request_schemas.header], responses={200: ''})
    def delete(self, request, board_pk):
        """
        게시판 삭제

        ## 게시판 삭제
        - 게시판을 삭제합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        """
        board = Board.objects.get(pk=board_pk)
        board.delete()
        return Response()


@api_view(['GET'])
def MainArticles(request, board_pk):
    """
    메인페이지 게시글 목록 조회

    ## 메인페이지 게시글 목록 조회
    - 메인페이지에 들어갈 게시글 목록 5개를 불러옵니다.
    """
    board = get_object_or_404(Board, pk=board_pk)
    articles = board.article_set.all().order_by('-created_at')[:5]
    serializer = ArticleSerializer(articles, many=True, context={'request': request})
    return Response(serializer.data)


class Articles(APIView):
    pagination_class = Pagination
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                   self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
    
    @swagger_auto_schema(responses={200: ArticleSerializer})
    def get(self, request, board_pk):
        """
        게시글 목록 조회

        ## 게시글 목록 조회
        - 게시글 list를 불러옵니다.
        - 페이지 
        - params : 유저(user=id)로 검색, 제목(title=id)으로 검색, 내용(content=id)으로 검색 
        - params : 정렬 방법(기본-최신순/댓글 많은 순(order=comments)/좋아요 많은 순(oder=likes))
        """
        user = request.GET.get('user', None)
        title = request.GET.get('title', None)
        content = request.GET.get('content', None)
        order = request.GET.get('order', None)

        if user:
            articles = Article.objects.filter(board=board_pk, user=user)
        elif title:
            articles = Article.objects.filter(board=board_pk, title__contains=title)
        elif content:
            articles = Article.objects.filter(board=board_pk, content__contains=content)
        else:
            articles = Article.objects.filter(board=board_pk)
        if order == 'comments':
            articles = articles.filter(board=board_pk).annotate(comments=Count('comment')).order_by('-comments')
        elif order == 'likes':
            articles = articles.filter(board=board_pk).annotate(likes=Count('like_users')).order_by('-likes')
        else:
            articles = articles.filter(board=board_pk).order_by('-created_at')
        page = self.paginate_queryset(articles)
        serializer_class = ArticleSerializer
        if page:
            serializer_articles = self.get_paginated_response(serializer_class(page, context={'request': request}, many=True).data)
        else:
            serializer_articles = serializer_class(articles, context={'request': request}, many=True)
        board = get_object_or_404(Board, pk=board_pk)
        serializer_board = BoardDetailSerializer(board)

        return Response({
            'board': serializer_board.data,
            'articles': serializer_articles.data
        })


    # 게시물 create - params : title, content
    @swagger_auto_schema(
        request_body=request_schemas.ArticleCreateRequest,
        manual_parameters=[request_schemas.header],
        responses={
            201: ArticleCreateSerializer
        }
    )
    def post(self, request, board_pk):
        """
        게시글 생성

        ## 게시글 생성
        - title, content를 받아 게시글을 생성합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        """
        serializer = ArticleCreateSerializer(data=request.data)
        board = Board.objects.get(pk=board_pk)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, board=board)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    
    @swagger_auto_schema(responses={200: ArticleDetailSerializer})
    def get(self, request, board_pk, article_pk):
        """
        게시글 상세 조회

        ## 게시글 상세 조회
        - 게시글 list를 불러옵니다.
        """
        article = Article.objects.get(pk=article_pk)
        serializer = ArticleDetailSerializer(article, context={'request': request})
        return Response(serializer.data)

    # 게시물 update - params : title, content
    @swagger_auto_schema(
        request_body=request_schemas.ArticleCreateRequest,
        manual_parameters=[request_schemas.header],
        responses={
            200: ArticleCreateSerializer
        }
    )
    def put(self, request, board_pk, article_pk):
        """
        게시글 수정

        ## 게시글 수정
        - title, content를 받아 게시글을 수정합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        - 글쓴이만 수정할 수 있습니다.
        """
        article = Article.objects.get(pk=article_pk)
        if request.user == article.user: 
            board = Board.objects.get(pk=board_pk)
            serializer = ArticleCreateSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, board=board)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


    @swagger_auto_schema(manual_parameters=[request_schemas.header], responses={200: ''})
    def delete(self, request, board_pk, article_pk):
        """
        게시글 삭제

        ## 게시글 삭제
        - 게시글을 삭제합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        - 글쓴이만 삭제할 수 있습니다.
        """
        article = Article.objects.get(pk=article_pk)
        if request.user == article.user:
            article.delete()
            return Response()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    # 댓글 create - params : content
    @swagger_auto_schema(
        request_body=request_schemas.CommentCreateRequest,
        manual_parameters=[request_schemas.header],
        responses={
            201: CommentCreateSerializer
        }
    )
    def post(self, request, board_pk, article_pk):
        """
        댓글 생성

        ## 댓글 생성
        - content을 받아 댓글을 생성합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        """
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    
    @swagger_auto_schema(
        request_body=request_schemas.CommentCreateRequest,
        manual_parameters=[request_schemas.header],
        responses={
            200: CommentCreateSerializer
        }
    )
    def put(self, request, board_pk, article_pk, comment_pk):
        """
        댓글 수정

        ## 댓글 수정
        - content를 받아 댓글을 수정합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        - 글쓴이만 수정할 수 있습니다.
        """
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            serializer = CommentCreateSerializer(comment, data=request.data)
            article = get_object_or_404(Article, pk=article_pk)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, article=article)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


    @swagger_auto_schema(manual_parameters=[request_schemas.header], responses={200: ''})
    def delete(self, request, board_pk, article_pk, comment_pk):
        """
        댓글 삭제

        ## 댓글 삭제
        - 댓글을 삭제합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        - 글쓴이만 삭제할 수 있습니다.
        """
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
            return Response()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@swagger_auto_schema(
    method='post',
    manual_parameters=[request_schemas.header], 
    responses={200: ''}
)
@api_view(['POST'])
def like_article(request, article_pk):
    """
    게시글 좋아요

    ## 게시글 좋아요
    - 게시글의 좋아요 기능입니다. 
    - 사용자가 이미 좋아요를 누른 게시글이라면 좋아요를 취소합니다.
    - 로그인한 사용자만 요청할 수 있습니다.
    """
    article = get_object_or_404(Article, pk=article_pk)
    # 이미 좋아요 한 경우
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        return Response(status=200)
    else:
        article.like_users.add(request.user)
    return Response(status=200)


@swagger_auto_schema(
    method='post',
    manual_parameters=[request_schemas.header], 
    responses={200: ''}
)
@api_view(['POST'])
def favorite(request, board_pk):
    """
    게시판 즐겨찾기

    ## 게시판 즐겨찾기
    - 게시판의 즐겨찾기 기능입니다. 
    - 사용자가 이미 즐겨찾기 한 게시판이라면 즐겨찾기를 취소합니다.
    - 로그인한 사용자만 요청할 수 있습니다.
    """
    board = get_object_or_404(Board, pk=board_pk)
    # 이미 즐겨찾기 한 경우
    if request.user in board.favorite_users.all():
        board.favorite_users.remove(request.user)
    else:
        board.favorite_users.add(request.user)
    return Response(status=200)
