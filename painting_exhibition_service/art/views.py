from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from .services.art_service import (
    check_is_artist,
    create_art,
)


class ArtView(APIView):

    def post(self, request):
        if check_is_artist(request.user):
            create_art(request.data, request.user)
            return Response({"detail" : "작품을 등록하였습니다."}, status=status.HTTP_200_OK)
        return Response({"detail" : "관리자만이 접근이 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)