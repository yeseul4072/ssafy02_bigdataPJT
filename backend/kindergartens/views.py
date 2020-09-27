# django
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# DRF
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# App - community
from .models import Kindergarten, Weight

# data analysis
import pandas as pd

# recommendation algorithm
import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from bigdata import recommend
from haversine import haversine


class Recommend(APIView):
    def get(self, request):
        # weight 테이블에 요청 유저 없는 경우(아무 활동도 하지 않은 경우)
        # 요청 유저와 가까운 유저 없는 경우

        # request 유저 근처에 있는 어린이집id
        latitude = request.user.latitude
        longitude = request.user.longitude
        user_position = (latitude, longitude)

        near_kindergartens_id = []
        for kindergarten in Kindergarten.objects.all():
            if haversine(user_position, (kindergarten.lat, kindergarten.lng)) <= 5:
                near_kindergartens_id.append(kindergarten.id)
        
        # 어린이집-어린이집feature 행렬(근처)
        df = pd.DataFrame(Kindergarten.objects.filter(id__in=near_kindergartens_id).values('id','school_bus','general','infants','disabled','disabled_integration','after_school','after_school_inclusion','extension','holiday','all_day','part_time','office','public','private','family','corporate','cooperation','welfare','has_extension_class','language','culture','sport','science'))
        kindergarten_df = df.set_index('id')
                        
        # 추천 유저 주변에 사는 유저 목록 
        near_users_id = []
        User = get_user_model()
        for q in Weight.objects.all():
            user = User.objects.get(pk=q.user_id)
            if haversine(user_position, (user.latitude, user.longitude)) <= 5 and q.kindergarten_id in near_kindergartens_id:
                near_users_id.append(q.id)
        near_users = pd.DataFrame(Weight.objects.filter(id__in=near_users_id).values('user_id', 'kindergarten_id', 'weight'))
        # print(near_users)

        # 유저-어린이집 가중치 행렬
        users_weight = recommend.parse_user_data(near_users, near_kindergartens_id)
        # print(users_weight)
        # 추천해줄 유저 행만 선택
        user_df = users_weight.loc[request.user.id]
        # 유저-어린이집feature 행렬
        preference_df = recommend.get_preference(kindergarten_df, user_df)
        # content-based 추천
        contents_recommend = recommend.recommend(kindergarten_df, preference_df, 10)
        # print(contents_recommend_df)
        # collaborative 추천
        user_df2 = users_weight.loc[[request.user.id],:]
        collabo_recommend = recommend.user_based_collaborative_filtering(users_weight, user_df2, 10)

        recommend_kindergartens = collabo_recommend + list(contents_recommend)
        return Response(recommend_kindergartens[:10])