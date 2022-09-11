from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from applicant.services.applicant_service import (
    create_apply,
)
# Create your views here.

class ApplicantView(APIView):
    """
    Applicant의 CRUD를 담당하는 View
    """
    def post(self, request):
        create_apply(request.data, request.user)
        return Response({"detail" : "게시글을 작성하였습니다."}, status=status.HTTP_200_OK)