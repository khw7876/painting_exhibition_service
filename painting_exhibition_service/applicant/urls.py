from django.urls import path

from . import views

urlpatterns = [
    path("", views.ApplicantView.as_view(), name="applicant_view"),
]