from rest_framework import serializers
from .models import Board, Favorite, Article, Comment
from accounts.serializers import UserSerializer, UserListSerializer


class BoardListSerializer(serializers.ModelSerializer):
    article_count = serializers.SerializerMethodField()
    favorite_yn = serializers.SerializerMethodField()
    def get_favorite_yn(self, obj):
        request = self.context.get('request', None)
        if obj.favorite_users.all():
            if obj.favorite_users.filter(id=request.user.id).exists():
                return 1
        return 0
    def get_article_count(self, obj):
        return obj.article_set.all().count()
    class Meta:
        model = Board
        fields = ['id', 'title', 'content', 'article_count', 'favorite_yn'] 


class BoardSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(source='user.id', required=False)
    class Meta:
        model = Board
        fields = '__all__'


class BoardDetailSerializer(serializers.ModelSerializer):
    favorite_yn = serializers.SerializerMethodField()
    article_count = serializers.SerializerMethodField()
    def get_favorite_yn(self, obj):
        request = self.context.get('request', None)
        if obj.favorite_users.filter(id=request.user.id).exists():
            return 1
        return 0
    def get_article_count(self, obj):
        return obj.article_set.all().count()
    class Meta:
        model = Board
        fields = ['id', 'title', 'favorite_yn', 'article_count']


class ArticleSerializer(serializers.ModelSerializer): 
    user = UserListSerializer(required=False)
    like_count = serializers.SerializerMethodField()
    like_yn = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    board = BoardListSerializer(required=False)
    def get_like_yn(self, obj):
        request = self.context.get('request', None)
        if request.user.is_authenticated: 
            if obj.like_users.filter(id=request.user.id).exists():
                return 1
        return 0
    def get_like_count(self, obj):
        return obj.like_users.count()
    def get_comment_count(self, obj):
        return obj.comment_set.count()
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'like_count', 'like_yn', 'comment_count', 'user', 'hit', 'board']


class ArticleCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    board = BoardSerializer(required=False)
    class Meta:
        model = Article
        fields = ['title', 'content', 'user', 'board']


class ArticleCommentSerializer(serializers.ModelSerializer):
    user = UserListSerializer(required=True)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'updated_at', 'user']


class ArticleDetailSerializer(serializers.ModelSerializer): 
    board_id = serializers.IntegerField(source='board.id')
    board_name = serializers.CharField(source='board.title')
    user = UserListSerializer()
    like_count = serializers.SerializerMethodField()
    like_yn = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    comments = ArticleCommentSerializer(source='comment_set', many=True)
    def get_like_count(self, obj):
        return obj.like_users.count()
    def get_like_yn(self, obj):
        request = self.context.get('request', None)
        if obj.like_users.filter(id=request.user.id).exists():
            return 1
        return 0
    def get_comment_count(self, obj):
        return obj.comment_set.count()
    class Meta:
        model = Article
        fields = ['board_id', 'board_name', 'user', 'id', 'title', 'content', 'created_at', 'updated_at', 'like_yn', 'like_count', 'comment_count', 'comments', 'hit']


class CommentCreateSerializer(serializers.ModelSerializer):
    user = UserListSerializer(required=False)
    article = ArticleCommentSerializer(required=False)
    class Meta:
        model = Comment
        fields = '__all__'