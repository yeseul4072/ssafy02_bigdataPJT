from drf_yasg import openapi
from rest_framework import serializers
from .models import Kindergarten, Weight, Review

header = openapi.Parameter(
    'Authorization',
    openapi.IN_HEADER,
    description='"Token {키값}"의 형태로 토큰을 입력하세요.',
    type=openapi.TYPE_STRING
)

