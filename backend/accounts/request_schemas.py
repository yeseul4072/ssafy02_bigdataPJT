from drf_yasg import openapi
from rest_framework import serializers


header = openapi.Parameter(
    'Authorization',
    openapi.IN_HEADER,
    description='"Token {키값}"의 형태로 토큰을 입력하세요.',
    type=openapi.TYPE_STRING
)

password = openapi.Parameter(
    'password',
    openapi.IN_QUERY,
    description='검사할 비밀번호를 입력하세요',
    type=openapi.TYPE_STRING
)

username = openapi.Parameter(
    'username',
    openapi.IN_QUERY,
    description='검사할 아이디를 입력하세요',
    type=openapi.TYPE_STRING
)

nickname = openapi.Parameter(
    'nickname',
    openapi.IN_QUERY,
    description='검사할 닉네임을 입력하세요',
    type=openapi.TYPE_STRING
)

email = openapi.Parameter(
    'email',
    openapi.IN_QUERY,
    description='검사할 이메일을 입력하세요',
    type=openapi.TYPE_STRING
)