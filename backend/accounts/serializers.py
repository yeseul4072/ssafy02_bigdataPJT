from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'nickname']

class CustomRegisterSerializer(serializers.ModelSerializer, RegisterSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'latitude', 'longitude',
            'address', 'nickname', 'is_director', 'kindergarten_id'
        ]

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user