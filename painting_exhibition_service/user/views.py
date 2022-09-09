from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSignupSerializer

# Create your views here.
class UserView(APIView):
    """
    회원정보 조회 및 회원가입
    """
    def post(self, request: Request) -> Response:
        user_data_serializer = UserSignupSerializer(data=request.data)
        user_data_serializer.is_valid(raise_exception=True)
        user_data_serializer.save()
        return Response({"detail": "회원가입을 성공하였습니다"}, status=status.HTTP_200_OK)
