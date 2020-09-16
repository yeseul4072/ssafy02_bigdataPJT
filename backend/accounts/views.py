from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
# swagger
from drf_yasg.utils import swagger_auto_schema
from . import request_schemas


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