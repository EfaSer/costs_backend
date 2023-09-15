from django.urls import path
from .views import ApiListAPIView


urlpatterns = [
  path("api/", ApiListAPIView.as_view())
]