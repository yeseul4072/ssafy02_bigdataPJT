from django.shortcuts import redirect, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
# from spc_pjt.settings.base import Secrets, BASE_DIR
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from .validators import CustomMinimumLengthValidator, CustomCommonPasswordValidator, CustomNumericPasswordValidator
from django.core.validators import validate_email

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

@swagger_auto_schema(method='get', manual_parameters=[request_schemas.password], responses={200: 'OK'},)
@api_view(['GET'])
def password_validate(request):
    """
    비밀번호 중복 체크

    ## 비밀번호 중복 체크
    - 사용 가능한 비밀번호인지 체크합니다.
    - 사용 가능하면 200, 불가능하면 400 상태코드를 반환합니다.
    """
    password = request.GET.get('password')
    if not CustomMinimumLengthValidator().validate(password): return HttpResponse('비밀번호가 너무 짧습니다. 최소한 8글자 이상의 비밀번호를 사용해야 합니다.', status=400)
    if not CustomCommonPasswordValidator().validate(password): return HttpResponse('너무 일상적인 비밀번호입니다.', status=400)
    if not CustomNumericPasswordValidator().validate(password): return HttpResponse('비밀번호가 모두 숫자로 이루어져 있습니다.', status=400)
    return HttpResponse('적절한 비밀번호입니다.', status=200)
    
@swagger_auto_schema(method='get', manual_parameters=[request_schemas.username], responses={200: 'OK'},)
@api_view(['GET'])
def username_validate(request):
    """
    아이디 중복 체크

    ## 아이디 중복 체크
    - 사용 가능한 아이디인지 체크합니다.
    - 사용 가능하면 200, 불가능하면 400 상태코드를 반환합니다.
    """
    username = request.GET.get('username')
    try:
        if User.objects.get(username=username):
            return HttpResponse('이미 있는 아이디입니다.', status=400)
    except:
        return HttpResponse('사용할 수 있는 아이디입니다.', status=200)

@swagger_auto_schema(method='get', manual_parameters=[request_schemas.nickname], responses={200: 'OK'},)
@api_view(['GET'])
def nickname_validate(request):
    """
    닉네임 중복 체크

    ## 닉네임 중복 체크
    - 사용 가능한 닉네임인지 체크합니다.
    - 사용 가능하면 200, 불가능하면 400 상태코드를 반환합니다.
    """
    nickname = request.GET.get('nickname')
    try:
        if User.objects.get(nickname=nickname):
            return HttpResponse('이미 있는 닉네임입니다.', status=400)
    except:
        return HttpResponse('사용할 수 있는 닉네임입니다.', status=200)

@swagger_auto_schema(method='get', manual_parameters=[request_schemas.email], responses={200: 'OK'},)
@api_view(['GET'])
def email_validate(request):
    """
    이메일 중복 체크

    ## 이메일 중복 체크
    - 사용 가능한 이메일인지 체크합니다.
    - 사용 가능하면 200, 불가능하면 400 상태코드를 반환합니다.
    """
    email = request.GET.get('email')
    try:
        validate_email(email)
    except:
        return HttpResponse('이메일 형식이 적절하지 않습니다.', status=400)
    try:
        if User.objects.get(email=email):
            return HttpResponse('이미 있는 이메일입니다.', status=400)
    except:
        return HttpResponse('사용할 수 있는 이메일입니다.', status=200)

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