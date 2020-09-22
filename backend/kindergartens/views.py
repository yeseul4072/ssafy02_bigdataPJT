# django
from django.shortcuts import get_object_or_404

# DRF
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# App - community
from .models import Kindergarten

# data analysis
import pandas as pd

# recommendation algorithm
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from bigdata import recommend
from haversine import haversine


class Recommend(APIView):
    def get(self, request):
        # request유저 근처에 있는 어린이집만 추출
        latitude = 129.009234
        longitude = 35.2194848
        user_position = (129.009234, 35.2194848)
        kindergartens = Kindergarten.objects.all()
        near_kindergartens = [kindergarten for kindergarten in kindergartens if haversine(user_position, (kindergarten.lat, kindergarten.lng)) <= 5]
        print(near_kindergartens)
        # DB에서 알고리즘에 사용할 컬럼만 추출 
        kindergarten_arr = list(Kindergarten.objects.all().values('id','school_bus','general','infants','disabled','disabled_integration','after_school','after_school_inclusion','extension','holiday','all_day','part_time','office','public','private','family','corporate','cooperation','welfare','has_extension_class','language','culture','sport','science'))
        df = pd.DataFrame(kindergarten_arr)
        df = pd.DataFrame(data=kindergarten_arr, index=list(df['id']))
        kindergarten_df = df[df.columns.difference(['id'])]
        # print(kindergarten_df)
        # 유저-어린이집 가중치
        user_idx = 0
        user_weight = recommend.get_weight(user_idx, len(kindergarten_matrix))
        # 유저-어린이집feature 행렬
        user_preference = recommend.get_preference(kindergarten_matrix,user_weight)
        # 추천 
        kidergarten_recommended = recommend.recommend(kindergarten_matrix,user_preference)
        # print(kidergarten_recommended)


