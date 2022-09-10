from django.db import models
from django.core.validators import RegexValidator

from user.models import User as UserModel

# Create your models here.

class ApplicantModel(models.Model):
    user = models.ForeignKey(UserModel, related_name='artist_names', on_delete=models.CASCADE)
    name = models.CharField("성명",max_length=16)
    gender = models.ForeignKey("성별", on_delete=models.SET_NULL, null=True)
    birthday = models.CharField("생일", max_length = 11)
    email = models.CharField("이메일", max_length=120)
    phone_number = models.CharField("연락처", max_length = 13)
    status = models.ForeignKey("상태", on_delete=models.SET_NULL, null=True)
    apply_date = models.DateTimeField("신청날짜", auto_now_add=True)

    class Meta:
        db_table = 'applicant'
    def __str__(self):
        return self.name

class Status(models.Model):

    STATUS_CHOICES = (
        ("waiting", "대기중"),
        ("accept", "수락"),
        ("disaccept", "반려"),
    )
    status = models.CharField("상태", max_length=20, choices=STATUS_CHOICES, default="waiting")
    
    class Meta:
        db_table = 'status'
    def __str__(self):
        return self.name

class Gender(models.Model):

    GENDER_CHOICES = (
        ("undefined", "미선택"),
        ("male", "남성"),
        ("female", "여성"),
    )
    gender = models.CharField("성별", max_length=20, choices=GENDER_CHOICES, default="undefined")
    
    class Meta:
        db_table = 'gender'
    def __str__(self):
        return self.gender


