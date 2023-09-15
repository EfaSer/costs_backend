from rest_framework import generics
from .models import Cost
from .serializers import ApiSerializer


class ApiListAPIView(generics.ListCreateAPIView):
  serializer_class = ApiSerializer
  queryset = Cost.objects.all()