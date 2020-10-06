from drf_yasg import openapi
from rest_framework import serializers
from .models import Kindergarten, Weight, Review

header = openapi.Parameter(
    'Authorization',
    openapi.IN_HEADER,
    description='"Token {키값}"의 형태로 토큰을 입력하세요.',
    type=openapi.TYPE_STRING
)


class ReviewCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'score_teacher', 'score_director', 'score_environment', 'pros', 'cons']


latitude = openapi.Parameter(
    'lat',
    openapi.IN_QUERY,
    description='위도를 입력하세요.',
    type=openapi.TYPE_NUMBER
)

longitude = openapi.Parameter(
    'lng',
    openapi.IN_QUERY,
    description='경도를 입력하세요.',
    type=openapi.TYPE_NUMBER
)
