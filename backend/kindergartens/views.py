# django
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from django.db.models import Avg, Count, Q

# DRF
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

# App - community
from .models import Kindergarten, Weight, Review, Borough, Village
from .serializers import (KindergartenListSerializer, ActivatedReviewSerializer, ReviewSerializer, KindergartenDetailSerializer, 
ReviewCreateSerializer, BoroughSerializer, VillageSerializer, KindergartenImageSerializer)

# data analysis
import pandas as pd

# recommendation algorithm
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from bigdata import recommend
from haversine import haversine

# swagger
from drf_yasg.utils import swagger_auto_schema
from . import request_schemas


"""
런처 페이지
"""

@swagger_auto_schema(method='get', responses={200: 'OK'})
@api_view(['GET'])
def Count(request):
    """
    어린이집, 유저, 리뷰 수 조회

    ## 어린이집, 유저, 리뷰 수 조회
    - 전체 어린이집, 유저, 리뷰 수를 조회합니다.
    """
    User = get_user_model()
    users = User.objects.all()
    kindergartens = Kindergarten.objects.all()
    reviews = Review.objects.all()
    return JsonResponse({'kindergartens': kindergartens.count(), 'users': users.count(), 'reviews': reviews.count()})


"""
메인 페이지
"""
class FBasedRecommend(APIView):
    @swagger_auto_schema(manual_parameters=[request_schemas.header], responses={200: KindergartenListSerializer})
    def get(self, request):
        """
        메인페이지 어린이집 추천

        ## 메인페이지 어린이집 추천
        - 유저가 선호하는 feature에 해당하는 어린이집 정보 조회
        - 유저의 활동에 따라 response가 변함
        """
        if request.user.is_authenticated:
            latitude = request.user.latitude
            longitude = request.user.longitude
            user_position = (latitude, longitude)

            near_kindergartens_id = []

            for kindergarten in Kindergarten.objects.all():
                if haversine(user_position, (kindergarten.lat, kindergarten.lng)) <= 5:
                    near_kindergartens_id.append(kindergarten.id)

            if len(request.user.weight_kindergartens.all()):
                # 유저-어린이집 가중치 행렬
                user = pd.DataFrame(Weight.objects.filter(user=request.user, kindergarten_id__in=near_kindergartens_id).values('user_id', 'kindergarten_id', 'weight'))
                user_df = recommend.parse_user_data(user, near_kindergartens_id)
                # 유저-어린이집feature 행렬
                df = pd.DataFrame(Kindergarten.objects.filter(id__in=near_kindergartens_id).values('id','school_bus','general','infants','disabled','disabled_integration','after_school','after_school_inclusion','extension','holiday','all_day','part_time','office','public','private','family','corporate','cooperation','welfare','has_extension_class','language','culture','sport','science'))
                kindergarten_df = df.set_index('id')
                preference_df = recommend.get_preference(kindergarten_df, user_df)
                # request 유저가 선호하는 feature 1, 2, 3위
                preference_df = preference_df.transpose()
                preference_df = preference_df.sort_values(by=0, ascending=False)
                features = preference_df[0].head(2).index
                # print(features)
                # feature가 1인 어린이집만 추출  
                features = (list(features))
                f1 = features[0]
                f2 = features[1]
                kindergartens1 = Kindergarten.objects.filter(**{f1: 1}, id__in=near_kindergartens_id).order_by('?')[:6]
                temp = [kindergarten['id'] for kindergarten in kindergartens1.values()]
                kindergartens2 = Kindergarten.objects.filter(**{f2: 1}, id__in=near_kindergartens_id).exclude(id__in=temp).order_by('?')[:6]
                
                data = []
                for k in kindergartens1:
                    if k.review_set.all().exists():
                        count_all = k.review_set.count() * 3
                        scores_teacher = k.review_set.aggregate(Sum('score_teacher')).get('score_teacher__sum')
                        scores_director = k.review_set.aggregate(Sum('score_director')).get('score_director__sum')
                        scores_environment = k.review_set.aggregate(Sum('score_environment')).get('score_environment__sum')
                        score_avg = (scores_teacher + scores_director + scores_environment) / count_all
                    else:
                        score_avg = 0
                    # 유저-어린이집 거리
                    distance = haversine(user_position, (k.lat, k.lng))
                    
                    data.append({
                        'id': k.id,
                        'feature': f1,
                        'lat': k.lat,
                        'lng': k.lng,
                        'organization_name': k.organization_name,
                        'reviews_count': k.review_set.count(),
                        'score_avg': score_avg,
                        'distance': distance,
                        'features': {
                            'school_bus': k.school_bus, 'general': k.general , 'infants': k.infants, 'disabled': k.disabled, 'disabled_integration': k.disabled_integration, 'after_school': k.after_school, 'after_school_inclusion': k.after_school_inclusion,
                            'extension': k.extension, 'holiday': k.holiday, 'all_day': k.all_day, 'part_time': k.part_time, 'office': k.office, 'public': k.public, 'private': k.private, 'family': k.family, 'corporate': k.corporate, 
                            'cooperation': k.cooperation, 'welfare': k.welfare, 'has_extension_class': k.has_extension_class, 'language': k.language, 'culture': k.culture, 'sport': k.sport, 'science': k.science, 'has_extension_class': k.has_extension_class, 'extension': k.extension
                        }
                    })
                for k2 in kindergartens2:
                    if k2.review_set.all().exists():
                        count_all = k2.review_set.count() * 3
                        scores_teacher = k2.review_set.aggregate(Sum('score_teacher')).get('score_teacher__sum')
                        scores_director = k2.review_set.aggregate(Sum('score_director')).get('score_director__sum')
                        scores_environment = k2.review_set.aggregate(Sum('score_environment')).get('score_environment__sum')
                        score_avg = (scores_teacher + scores_director + scores_environment) / count_all
                    else:
                        score_avg = 0
                    # 유저-어린이집 거리
                    distance = haversine(user_position, (k2.lat, k2.lng))
                    data.append({
                        'id': k2.id,
                        'feature': f2,
                        'lat': k2.lat,
                        'lng': k2.lng,
                        'organization_name': k2.organization_name,
                        'reviews_count': k2.review_set.count(),
                        'score_avg': score_avg,
                        'distance': distance,
                        'features': {
                            'school_bus': k2.school_bus, 'general': k2.general , 'infants': k2.infants, 'disabled': k2.disabled, 'disabled_integration': k2.disabled_integration, 'after_school': k2.after_school, 'after_school_inclusion': k2.after_school_inclusion,
                            'extension': k2.extension, 'holiday': k2.holiday, 'all_day': k2.all_day, 'part_time': k2.part_time, 'office': k2.office, 'public': k2.public, 'private': k2.private, 'family': k2.family, 'corporate': k2.corporate, 
                            'cooperation': k2.cooperation, 'welfare': k2.welfare, 'has_extension_class': k2.has_extension_class, 'language': k2.language, 'culture': k2.culture, 'sport': k2.sport, 'science': k2.science, 'has_extension_class': k2.has_extension_class, 'extension': k2.extension
                        }
                    })
                return JsonResponse(data, safe=False)
            else:
                kindergartens = Kindergarten.objects.filter(id__in=near_kindergartens_id)[:12]
                serializer = KindergartenListSerializer(kindergartens, context={'request': request}, many=True)
                return Response(serializer.data)
        else:
            kindergartens = Kindergarten.objects.all().order_by('?')[:12]
            serializer = KindergartenListSerializer(kindergartens, context={'request': request}, many=True)
            return Response(serializer.data)


class ReviewActivated(APIView):
    @swagger_auto_schema(responses={200: ActivatedReviewSerializer})
    def get(self, request):
        """
        뜨는 리뷰 조회

        ## 뜨는 리뷰를 조회합니다.
        - 리뷰를 최신순으로 정렬하여 5개 보여줍니다.
        """
        # 좋아요, 최신순 정렬 select like_users
        # review_list = Review.objects.annotate(like_count=Count('like_users')).order_by('-count', '-created_at')[:5]
        # review_list = Review.objects.raw("""
        # select kr.*, ifnull(kr_like.like_count, 0) as like_count
        #   from kindergartens_review kr
		# 	   left outer join
		# 	   (
        #        select count(1) as like_count, review_id
        #          from kindergartens_review_like_users
		# 	 group by review_id
        #        )kr_like
        #        on
        #        kr.id = kr_like.review_id
        # order by like_count, created_at desc
        # limit 5;
        # """)
        review_list = Review.objects.order_by('-created_at')[:5]
        serializer = ActivatedReviewSerializer(review_list, many=True)
        return Response(serializer.data)

"""
어린이집 조회 페이지
"""
class KindergartenDetail(APIView):
    @swagger_auto_schema(responses={200: KindergartenDetailSerializer})
    def get(self, request, kindergarten_pk):
        """
        어린이집 디테일 조회

        ## 어린이집 디테일 조회
        - 어린이집 디테일 페이지에서 필요한 어린이집 데이터를 조회합니다.
        - 인증된 유저는 어린이집 가중치가 더해집니다.
        """
        kindergarten = Kindergarten.objects.get(pk=kindergarten_pk)
        serializer = KindergartenDetailSerializer(kindergarten, context={'request': request})
        # 가중치 더하기
        if request.user.is_authenticated:
            try:
                weight = Weight.objects.get(user=request.user, kindergarten=kindergarten)
                weight.weight += 1
                weight.save()
            except:
                weight = Weight.objects.create(user=request.user, kindergarten=kindergarten, weight=1)
        return Response(serializer.data)


class Pagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'

class Reviews(APIView):
    pagination_class = Pagination
    serializer_class = ReviewSerializer
   
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                   self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    @swagger_auto_schema(responses={200: ReviewSerializer})
    def get(self, request, kindergarten_pk):
        """ 
        어린이집 리뷰 리스트 조회

        ## 어린이집 리뷰 리스트 조회
        - 어린이집 디테일 페이지에서 필요한 리뷰 리스트를 조회합니다.
        - 한번에 응답하는 리뷰는 5개입니다.
        """
        instance =  Review.objects.filter(kindergarten=kindergarten_pk).order_by('-created_at')
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, context={'request': request}, many=True).data)
        else:
            serializer = self.serializer_class(instance, context={'request': request}, many=True)
        return Response(serializer.data) 
    
    @swagger_auto_schema(
        request_body=request_schemas.ReviewCreateRequest,
        manual_parameters=[request_schemas.header],
        responses={
            200: ReviewCreateSerializer
        }
    )
    def post(self, request, kindergarten_pk):
        """
        리뷰 생성

        ## 리뷰 생성
        - title을 받아 리뷰를 생성합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        """
        kindergarten = get_object_or_404(Kindergarten, pk=kindergarten_pk)
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, kindergarten=kindergarten)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    @swagger_auto_schema(manual_parameters=[request_schemas.header], responses={200: ''})
    def delete(self, request, kindergarten_pk, review_pk):
        """
        리뷰 삭제

        ## 리뷰 삭제
        - 리뷰를 삭제합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        """
        review = get_object_or_404(Review, pk=review_pk)
        review.delete()
        return Response()

    @swagger_auto_schema(
        request_body=request_schemas.ReviewCreateRequest,
        manual_parameters=[request_schemas.header],
        responses={
            200: ReviewCreateSerializer
        }
    )
    def put(self, request, kindergarten_pk, review_pk):
        """
        리뷰 수정 

        ## 리뷰 수정
        - 리뷰를 수정할 수 있습니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        """
        kindergarten = get_object_or_404(Kindergarten, pk=kindergarten_pk)
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewCreateSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, kindergarten=kindergarten)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    manual_parameters=[request_schemas.header], 
    responses={200: ''}
)
@api_view(['POST'])
def like_review(request, review_pk):
    """
    리뷰 좋아요

    ## 리뷰 좋아요 
    - 사용자가 이미 좋아요를 누른 리뷰라면 좋아요를 취소합니다.
    - 로그인한 사용자만 요청할 수 있습니다.
    """
    review = get_object_or_404(Review, pk=review_pk)
    # 이미 좋아요 한 경우
    if review.like_users.filter(id=request.user.id).exists():
        review.like_users.remove(request.user.id)
        return Response(status=200)
    else:
        review.like_users.add(request.user.id)
    return Response(status=200)


"""
어린이집 리스트 페이지
"""
class Kindergartens(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            request_schemas.latitude,
            request_schemas.longitude
        ],
        responses={200: ReviewSerializer}
    )
    def get(self, request):
        """ 
        검색 어린이집 리스트 조회

        ## 검색 어린이집 리스트 조회
        - 검색 시 입력한 위치 반경 2km 내 어린이집을 조회합니다. 
        """
        lat = float(request.GET.get('lat', None))
        lng = float(request.GET.get('lng', None))
        # 반경 2km
        condition1 = (
            Q(lat__range = (lat - 0.01, lat + 0.01))
        )
        condition2 = (
            Q(lng__range = (lng - 0.015, lng + 0.015))
        )
        instance = Kindergarten.objects.filter(condition1 & condition2)
        serializer = KindergartenListSerializer(instance, context={'request': request}, many=True)
        return Response(serializer.data)



class Recommend(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        """ 
        추천 어린이집 조회 (수정 필요)

        ## 추천 어린이집 조회
        - 사용자 위치와 가중치 값을 이용해 추천된 어린이집을 조회합니다.
        - 로그인한 사용자만 요청할 수 있습니다.
        """
        # request 유저 근처에 있는 어린이집id
        latitude = request.user.latitude
        longitude = request.user.longitude
        user_position = (latitude, longitude)

        near_kindergartens_id = []
        for kindergarten in Kindergarten.objects.all():
            if haversine(user_position, (kindergarten.lat, kindergarten.lng)) <= 5:
                near_kindergartens_id.append(kindergarten.id)

        # weight 테이블에 요청 유저 없는 경우(아무 활동도 하지 않은 경우) => 근처 어린이집 추천
        if len(request.user.weight_kindergartens.all()):
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
            print(preference_df)
            # content-based 추천
            contents_recommend = recommend.recommend(kindergarten_df, preference_df, 10)
            # print(contents_recommend_df)
            # collaborative 추천
            user_df2 = users_weight.loc[[request.user.id],:]
            collabo_recommend = recommend.user_based_collaborative_filtering(users_weight, user_df2, 10)

            recommend_kindergartens = collabo_recommend + list(contents_recommend)
            return Response(recommend_kindergartens[:10])
        else:
            return Response(near_kindergartens_id)

"""
어린이집 찜
"""
@swagger_auto_schema(method='post', manual_parameters=[request_schemas.header], responses={200: 'OK'})
@api_view(['POST'])
def WishList(request, kindergarten_pk):    
    """ 
    어린이집 찜하기

    ## 어린이집 찜하기
    - 어린이집 찜 기능입니다.
    - 이미 찜 한 어린이집은 찜을 취소합니다.
    - 로그인한 사용자만 요청할 수 있습니다.
    """
    kindergarten = get_object_or_404(Kindergarten, pk=kindergarten_pk)
    try:
        weight = Weight.objects.get(user=request.user, kindergarten=kindergarten)
    except:
        weight = Weight.objects.create(user=request.user, kindergarten=kindergarten, weight=0)
    if kindergarten.wish_users.filter(id=request.user.id).exists():
        kindergarten.wish_users.remove(request.user)
        # 가중치 빼기
        weight.weight -= 5
        weight.save()
    else:
        kindergarten.wish_users.add(request.user)
        # 가중치 더하기
        weight.weight += 5
        weight.save()
    return Response(status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated, IsAdminUser])
@api_view(['POST'])
def kindergarten_image(request, kindergarten_pk):
    """
    어린이집 이미지 업로드

    ## 어린이집 이미지 업로드
    ### 관리자만 수행할 수 있습니다.
    """
    kindergarten = get_object_or_404(Kindergarten, pk=kindergarten_pk)
    serializer = KindergartenImageSerializer(kindergarten, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def boroughs(request):
    """ 
    서울시의 군/구 조회

    ## 서울시의 군/구 조회
    """
    boroughs = Borough.objects.all()
    serializer = BoroughSerializer(boroughs, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def villages(request, borough_pk):
    """ 
    선택한 군/구에 속한 읍/면/동 조회 

    ## 선택한 군/구에 속한 읍/면/동 조회 
    """
    villages = Village.objects.filter(borough=borough_pk)
    serializer = VillageSerializer(villages, many=True)
    
    return Response(serializer.data)

