from django.contrib import admin
from .models import (
    Applicant, Status, Gender
)
# Register your models here.
admin.site.register(Applicant)
admin.site.register(Status)
admin.site.register(Gender)