from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

urlpatterns = [
    path("", views.UserView.as_view(), name="user_view"),
    path("<int:user_id>", views.UserView.as_view(), name="user_update"),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]