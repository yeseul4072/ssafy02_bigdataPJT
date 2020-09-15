from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Board, Favorite, Article, Comment
from .serializers import (BoardSerializer, ArticleSerializer, ArticleCreateSerializer, ArticleDetailSerializer,
CommentCreateSerializer, ArticleCommentSerializer)

# Create your views here.
class Boards(APIView):
  # 게시판 목록
  def get(self, request):
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)

  # 게시판 create - params : title
  def post(self, request):
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user)
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDetail(APIView):
  # 게시판 디테일 read
  def get(self, request, board_pk):
    board = Board.objects.get(pk=board_pk)
    serializer = BoardSerializer(board)
    return Response(serializer.data)

  # 게시판 update
  def put(self, request, board_pk):
    board = Board.objects.get(pk=board_pk)
    serializer = BoardSerializer(board, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # 게시판 delete
  def delete(self, request, board_pk):
      board = Board.objects.get(pk=board_pk)
      board.delete()
      return Response(status=200)


class Articles(APIView):
  # 게시물 list
  def get(self, request, board_pk):
    articles = Article.objects.filter(board=board_pk)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

  # 게시물 create - params : title, content
  def post(self, request, board_pk):
    serializer = ArticleCreateSerializer(data=request.data)
    board = Board.objects.get(pk=board_pk)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user, board=board)
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
  # 게시물 detail
  def get(self, request, board_pk, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleDetailSerializer(article)
    return Response(serializer.data)

  # 게시물 update - params : title, content
  def put(self, request, board_pk, article_pk):
    article = Article.objects.get(pk=article_pk)
    board = Board.objects.get(pk=board_pk)
    serializer = ArticleCreateSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, board=board)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # 게시물 delete
  def delete(self, request, board_pk, article_pk):
      article = Article.objects.get(pk=article_pk)
      article.delete()
      return Response(status=200)

  # 댓글 create - params : content
  def post(self, request, board_pk, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user, article=article)
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
  # 댓글 디테일 read
  def get(self, request, board_pk, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = ArticleCommentSerializer(comment)
    return Response(serializer.data)

  # 댓글 update
  def put(self, request, board_pk, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentCreateSerializer(comment, data=request.data)
    article = get_object_or_404(Article, pk=article_pk)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user, article=article)
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # 댓글 delete
  def delete(self, request, board_pk, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response(status=200)


@api_view(['GET'])
def like_article(request, board_pk, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  # 이미 좋아요 한 경우
  if request.user in article.like_user.all():
    article.like_user.remove(request.user)
    return Response(status=200)
  else:
    article.like_user.add(request.user)
  return Response(status=200)


@api_view(['GET'])
def favorite(request, board_pk):
  board = get_object_or_404(Board, pk=board_pk)
  # 이미 즐겨찾기 한 경우
  if request.user in board.favorite_user.all():
    board.favorite_user.remove(request.user)
  else:
    board.favorite_user.add(request.user)
  return Response(status=200)