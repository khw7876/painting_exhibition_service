from dataclasses import field
from rest_framework import serializers

from .models import Art as ArtModel

class ArtSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtModel
        fields = "__all__"