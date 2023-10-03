from rest_framework import viewsets
from rest_framework.response import Response
from .models import Cost, Category
from .serializers import ListCostSerializer, CreateCostSerializer, CategorySerializer
from rest_framework.exceptions import NotFound


class CostsViewSet(viewsets.ModelViewSet):
  queryset = Cost.objects.all()

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return ListCostSerializer
    else:
      return CreateCostSerializer


class CategorysViewSet(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()


class CostsCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ListCostSerializer
    queryset = Cost.objects.all()

    def retrieve(self, request, *args, **kwargs):
        category_slug = kwargs.get('category_slug')
        category = Category.objects.filter(slug=category_slug).first()
        if not category:
            raise NotFound('Category not found')
        queryset = self.queryset.filter(category=category)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
