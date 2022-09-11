from rest_framework import serializers

from .models import Applicant as ApplicantModel

VALID_EMAIL_LIST = ["naver.com","gmail.com", "google.com"]

class ApplicantSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data.get("email",'').split("@")[-1] not in VALID_EMAIL_LIST:
            raise serializers.ValidationError("네이버 이메일,구글 이메일만 사용 할 수 있습니다.")
        return data

    def get_applicant_gender(self, obj):
        if obj.gender:
            return obj.gender.gender
        return "None"

    class Meta:
        model = ApplicantModel
        fields = "__all__"