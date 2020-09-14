from rest_framework import serializers
from .models import Board, Favorite, Article, Comment


class BoardSerializer(serializers.ModelSerializer):
  user = serializers.IntegerField(source='user.id', required=False)
  class Meta:
    model = Board
    fields = '__all__'
