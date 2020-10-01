from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
from spc_pjt.settings.base import Secrets, BASE_DIR
import os
import requests
import json
# swagger
from drf_yasg.utils import swagger_auto_schema
from . import request_schemas


secret_file = os.path.join(BASE_DIR, 'secrets-local.json')
secrets = Secrets(secret_file)

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

# 카카오 소셜로그인
kakao_secret = secrets.get_secret('KAKAO')
REST_API_KEY = kakao_secret['REST_API_KEY']
REDIRECT_URI = kakao_secret['REDIRECT_URI']

class KakaoException(Exception):
    pass

# 인증 코드 요청
def kakao_login(request):
    kakao_code_request_url = f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code'
    return redirect(kakao_code_request_url)

def kakao_callback(request):
    # try:
    AUTHORIZE_CODE = request.GET.get('code')
    kakao_token_request_url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={AUTHORIZE_CODE}'
    
    # 인증 코드로 토큰 요청
    token_request = requests.get(kakao_token_request_url)
    token_response_json = token_request.json()
    error = token_response_json.get('error', None)

    if error is not None:
        raise KakaoException()
    USER_ACCESS_TOKEN = token_response_json.get('access_token')

    # 토큰으로 사용자 정보 API 호출
    headers = {'Authorization': f'Bearer {USER_ACCESS_TOKEN}'}
    profile_request = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers)
    profile_json = profile_request.json()
    print(profile_json)
    return redirect('http://childrenzip.site')