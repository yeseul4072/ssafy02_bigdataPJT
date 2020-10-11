from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


User = get_user_model()
host_url = 'http://childrenzip.site'

class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()
    
    def get_profile_image(self, obj):
        try: img = obj.profile_image.url
        except: return None
        return host_url + img

    class Meta:
        model = User
        exclude = ['password']

class UserListSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    def get_profile_image(self, obj):
        try: img = obj.profile_image.url
        except: return None
        return host_url + img

    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'profile_image']

class CustomRegisterSerializer(serializers.ModelSerializer, RegisterSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'latitude', 'longitude',
            'address', 'nickname', 'is_director', 'kindergarten_id', 'profile_image'
        ]

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)
    nickname = serializers.CharField(max_length=50, required=False)
    class Meta:
        model = User
        fields = ['nickname', 'profile_image', 'latitude', 'longitude', 'address']