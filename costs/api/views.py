from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Cost, Category
from .serializers import CostSerializer, CategorySerializer


class CostsViewSet(viewsets.ModelViewSet):
  serializer_class = CostSerializer
  queryset = Cost.objects.all()


class CategorysViewSet(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()

#class CostsCategoryViewSet(viewsets.ModelViewSet):
#  serializer_class = CostSerializer

#  #def get_queryset(self):
#  #  slug = self.kwargs.get('slug')
#  #  print("slug")

#  #  return Cost.objects.filter(slug=slug)

#  def get_queryset(self):
#    costs = get_object_or_404(
#        Cost,
#        pk=self.kwargs.get('slug')
#    )
#    return costs.costs_category.all()


def costs_category(request, slug):
  costs = Cost.objects.filter(category_id=3)
  print("asdvasvd")
  serializer = CostSerializer(costs, many=True)
  return Response(serializer.data)