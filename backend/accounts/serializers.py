from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = User
        fields = ['image', 'username', 'nickname']
        