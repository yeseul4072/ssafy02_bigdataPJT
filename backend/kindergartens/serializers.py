from rest_framework import serializers
from .models import Kindergarten, Weight, Review
from accounts.serializers import UserSerializer, UserListSerializer
from django.db.models import Avg, Sum


class KindergartenListSerializer(serializers.ModelSerializer):
    reviews_count = serializers.SerializerMethodField()
    score_avg = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    # image 추가 필요
    def get_reviews_count(self, obj):
        return obj.review_set.count()
    def get_score_avg(self, obj):
        count_all = obj.review_set.count() * 3
        scores_teacher = obj.review_set.aggregate(Sum('score_teacher')).get('score_teacher__sum')
        scores_director = obj.review_set.aggregate(Sum('score_director')).get('score_director__sum')
        scores_environment = obj.review_set.aggregate(Sum('score_environment')).get('score_environment__sum')
        return (scores_teacher + scores_director + scores_environment) / count_all
    def get_features(self, obj):
        features = {
            'school_bus': obj.school_bus,
            'general': obj.general,
            'infants': obj.infants,
            'disabled': obj.disabled,
            'disabled_integration': obj.disabled_integration,
            'after_school': obj.after_school,
            'after_school_inclusion': obj.after_school_inclusion,
            'extension': obj.extension,
            'holiday': obj.holiday,
            'all_day': obj.all_day,
            'part_time': obj.part_time, 
            'office': obj.office, 
            'public': obj.public, 
            'private': obj.private, 
            'family': obj.family, 
            'corporate': obj.corporate, 
            'cooperation': obj.cooperation, 
            'welfare': obj.welfare, 
            'has_extension_class': obj.has_extension_class, 
            'language': obj.language, 
            'culture': obj.culture, 
            'sport': obj.sport, 
            'science': obj.science, 
            'has_extension_class': obj.has_extension_class, 
            'extension': obj.extension
        }
        return features

    class Meta:
        model = Kindergarten
        fields = ['lat', 'lng', 'address', 'organization_name', 'reviews_count', 'score_avg', 'features']


class KindergartenDetailSerializer(KindergartenListSerializer):
    wishlist_yn = serializers.SerializerMethodField()
    def get_wishlist_yn(self, obj):
        request = self.context.get('request', None)
        if obj.wish_users.all():
            if request.user.id in obj.wish_users.all():
                return 1
        return 0
    class Meta(KindergartenListSerializer.Meta):
        fields = KindergartenListSerializer.Meta.fields + ['wishlist_yn', 'director_name', 'establishment_type', 'created_date', 'agency', 'tel', 'homepage', 'address', 'score', 'area_columns', 'area_info', 'building_columns', 'building_info', 'cctv_columns', 'cctv_info', 
        'area_per_cctv', 'age_by_class_columns', 'age_by_class_info', 'staff_columns', 'staff_info', 'continuous_columns', 'continuous_info', 'child_per_staff', 'fee_columns', 'fee_info', 'other_fee_columns', 'other_fee_info', 'special_activity_columns', 'special_activity_info',
        'monthly_fee', 'zero_year_old', 'one_year_old', 'two_year_old', 'three_year_old', 'four_year_old', 'five_year_old', 'poisoning_columns', 'poisoning_info', 'air_quality_columns', 'air_quality_info', 'disinfection_columns', 'disinfection_info', 'water_quality_columns', 'water_quality_info',
        'rating_certificate_columns', 'rating_certificate_info', 'rating_history_columns', 'rating_history_info', 'extension_class_status_columns', 'extension_class_status_info', 'extension_class_program_columns', 'extension_class_program_info']
        

class ActivatedReviewSerializer(serializers.ModelSerializer):
    kindergarten = KindergartenListSerializer()
    avg_score = serializers.SerializerMethodField()

    def get_avg_score(self, obj):
        return (obj.score_teacher + obj.score_director + obj.score_environment) / 3

    class Meta:
        model = Review
        fields = ['title', 'avg_score', 'pros', 'cons', 'kindergarten']


class ReviewSerializer(serializers.ModelSerializer):
    like_yn = serializers.SerializerMethodField()
    avg_score = serializers.SerializerMethodField()

    def get_like_yn(self, obj):
        request = self.context.get('request', None)
        if obj.like_users.all():
            if request.user.id in list(obj.like_users.all().values_list('id', flat=True)):
                return 1
        return 0

    def get_avg_score(self, obj):
        return (obj.score_teacher + obj.score_director + obj.score_environment) / 3

    class Meta:
        model = Review
        exclude = ['like_users', 'kindergarten']