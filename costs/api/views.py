from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Cost, Category
from .serializers import CostSerializer, CategorySerializer
from rest_framework.exceptions import NotFound


class CostsViewSet(viewsets.ModelViewSet):
  serializer_class = CostSerializer
  queryset = Cost.objects.all()


class CategorysViewSet(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()


class CostsCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CostSerializer
    queryset = Cost.objects.all()

    def retrieve(self, request, *args, **kwargs):
        category_slug = kwargs.get('category_slug')
        category = Category.objects.filter(slug=category_slug).first()
        if not category:
            raise NotFound('Category not found')
        queryset = self.queryset.filter(category=category)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
