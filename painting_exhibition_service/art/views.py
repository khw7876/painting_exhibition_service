from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from .services.art_service import (
    check_is_artist,
)


class ArtView(APIView):

    def post(self, request):
        if check_is_artist(request.user):
            return Response()
        return Response({"detail" : "관리자만이 접근이 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)