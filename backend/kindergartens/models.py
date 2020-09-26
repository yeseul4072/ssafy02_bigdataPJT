from django.db import models
from django.conf import settings

# Create your models here.

class Kindergarten(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    lat = models.FloatField(null=True, blank=True, default=0.0)
    lng = models.FloatField(null=True, blank=True, default=0.0)
    organization_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=50)
    establishment_type = models.CharField(max_length=50)
    created_date = models.DateField()
    agency = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    homepage = models.TextField()
    address = models.CharField(max_length=255)
    school_bus = models.SmallIntegerField()
    grade = models.SmallIntegerField()
    start_time = models.IntegerField()
    finish_time = models.IntegerField()
    general = models.SmallIntegerField()
    infants = models.SmallIntegerField()
    disabled = models.SmallIntegerField()
    disabled_integration = models.SmallIntegerField()
    after_school = models.SmallIntegerField()
    after_school_inclusion = models.SmallIntegerField()
    extension = models.SmallIntegerField()
    holiday = models.SmallIntegerField()
    all_day = models.SmallIntegerField()
    part_time = models.SmallIntegerField()
    office = models.SmallIntegerField()
    public = models.SmallIntegerField()
    private = models.SmallIntegerField()
    family = models.SmallIntegerField()
    corporate = models.SmallIntegerField()
    cooperation = models.SmallIntegerField()
    welfare = models.SmallIntegerField()

    score = models.FloatField()
    area_columns = models.CharField(max_length=255)
    area_info = models.TextField()
    building_columns = models.CharField(max_length=255)
    building_info = models.TextField()
    cctv_columns = models.CharField(max_length=255)
    cctv_info = models.TextField()
    area_per_cctv = models.FloatField()
    
    age_by_class_columns = models.CharField(max_length=255)
    age_by_class_info = models.TextField()
    staff_columns = models.CharField(max_length=255)
    staff_info = models.TextField()
    continuous_columns = models.CharField(max_length=255)
    continuous_info = models.TextField()
    child_per_staff = models.FloatField()
    fee_columns = models.CharField(max_length=255)
    fee_info = models.TextField()
    other_fee_columns = models.CharField(max_length=255)
    other_fee_info = models.TextField()
    special_activity_columns = models.CharField(max_length=255)
    special_activity_info = models.TextField()
    monthly_fee = models.CharField(max_length=255)

    zero_year_old = models.CharField(max_length=20)
    one_year_old = models.CharField(max_length=20)
    two_year_old = models.CharField(max_length=20)
    three_year_old = models.CharField(max_length=20)
    four_year_old = models.CharField(max_length=20)
    five_year_old = models.CharField(max_length=20)

    poisoning_columns = models.CharField(max_length=255)
    poisoning_info = models.TextField()
    air_quality_columns = models.CharField(max_length=255)
    air_quality_info = models.TextField()
    disinfection_columns = models.CharField(max_length=255)
    disinfection_info = models.TextField()
    water_quality_columns = models.CharField(max_length=255)
    water_quality_info = models.TextField()
    rating_certificate_columns = models.CharField(max_length=255)
    rating_certificate_info = models.TextField()
    rating_history_columns = models.CharField(max_length=255)
    rating_history_info = models.TextField()
    extension_class_status_columns = models.CharField(max_length=255)
    extension_class_status_info = models.TextField()
    extension_class_program_columns = models.CharField(max_length=255)
    extension_class_program_info = models.TextField()
    has_extension_class = models.SmallIntegerField()
    language = models.SmallIntegerField()
    culture = models.SmallIntegerField()
    sport = models.SmallIntegerField()
    science = models.SmallIntegerField()
    other = models.SmallIntegerField()
    program_by_age = models.TextField()
    cctv_grade = models.IntegerField()
    staff_grade = models.IntegerField()

    
class Weight(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kindergarten = models.ForeignKey(Kindergarten, on_delete=models.CASCADE)
    weight = models.IntegerField()