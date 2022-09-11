from django.db import models
from django.core.validators import RegexValidator

from user.models import User as UserModel

# Create your models here.

class Applicant(models.Model):
    user = models.ForeignKey(UserModel, related_name='artist_names', on_delete=models.CASCADE)
    name = models.CharField("성명",max_length=16)
    gender = models.ForeignKey("Gender", on_delete=models.SET_NULL, null=True)
    birthday_regex = RegexValidator(regex = r'^([0-9]{4})-?([0-9]{2})-?([0-9]{2})$')
    birthday = models.CharField("생일",validators = [birthday_regex], max_length = 11, unique = False, null=True, blank=True)
    email = models.CharField("이메일", max_length=120)
    phone_regex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone_number= models.CharField("연락처",validators = [phone_regex], max_length = 13, unique = True, null=True, blank=True)
    status = models.ForeignKey("Status", on_delete=models.SET_NULL, null=True)
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
        return self.status

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


