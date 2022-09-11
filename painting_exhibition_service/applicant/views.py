from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from applicant.services.applicant_service import (
    create_apply,
    read_apply,
    check_admin,
    check_is_applied,
)
# Create your views here.

class ApplicantView(APIView):
    """
    Applicant의 CRUD를 담당하는 View
    """
    def get(self, request):
        if check_admin(request.user):
            applicant_serializer = read_apply()
            return Response(applicant_serializer, status=status.HTTP_200_OK)
        return Response({"detail" : "관리자만이 접근이 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        if check_is_applied(request.user):
            create_apply(request.data, request.user)
            return Response({"detail" : "작가신청을 완료하였습니다."}, status=status.HTTP_200_OK)
        return Response({"detail" : "이미 작가신청을 하였습니다."}, status=status.HTTP_400_BAD_REQUEST)