from django.shortcuts import redirect, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
# from spc_pjt.settings.base import Secrets, BASE_DIR
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
import os
import requests
import json
# swagger
from drf_yasg.utils import swagger_auto_schema
from . import request_schemas


# secret_file = os.path.join(BASE_DIR, 'secrets-local.json')
# secrets = Secrets(secret_file)

User = get_user_model()

# Create your views here.
@swagger_auto_schema(method='delete', manual_parameters=[request_schemas.header], responses={200: None},)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def user_delete(request):
    """
    유저 삭제

    ## 유저 삭제
    - 로그인 한 사용자만 요청할 수 있습니다.
    """
    request.user.delete()
    return HttpResponse(status=200)

@swagger_auto_schema(method='get', manual_parameters=[request_schemas.header], responses={200: UserSerializer},)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """
    로그인된 유저 프로필 정보

    ## 로그인된 유저 프로필 정보 확인
    - 로그인 된 유저의 프로필 정보를 가져옵니다.
    - 로그인 한 사용자만 요청할 수 있습니다.
    """
    user = get_object_or_404(User, id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=UserUpdateSerializer, manual_parameters=[request_schemas.header], responses={200: UserUpdateSerializer},)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_update(request):
    """
    유저 정보 변경

    ## 유저 정보 변경
    - 로그인 한 사용자만 요청할 수 있습니다.
    - 닉네임, 주소(위도 경도 포함), 프로필사진을 바꿀 수 있습니다.
    """
    user = get_object_or_404(User, id=request.user.id)
    serializer = UserUpdateSerializer(user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return HttpResponse(status=400)

# # 카카오 소셜로그인
# kakao_secret = secrets.get_secret('KAKAO')
# REST_API_KEY = kakao_secret['REST_API_KEY']
# REDIRECT_URI = kakao_secret['REDIRECT_URI']

# class KakaoException(Exception):
#     pass

# # 인증 코드 요청
# def kakao_login(request):
#     kakao_code_request_url = f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code'
#     return redirect(kakao_code_request_url)

# def kakao_callback(request):
#     # try:
#     AUTHORIZE_CODE = request.GET.get('code')
#     kakao_token_request_url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={AUTHORIZE_CODE}'
    
#     # 인증 코드로 토큰 요청
#     token_request = requests.get(kakao_token_request_url)
#     token_response_json = token_request.json()
#     error = token_response_json.get('error', None)

#     if error is not None:
#         raise KakaoException()
#     USER_ACCESS_TOKEN = token_response_json.get('access_token')

#     # 토큰으로 사용자 정보 API 호출
#     headers = {'Authorization': f'Bearer {USER_ACCESS_TOKEN}'}
#     profile_request = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers)
#     profile_json = profile_request.json()
#     print(profile_json)
#     return redirect('http://childrenzip.site')