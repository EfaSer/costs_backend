from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CostsViewSet, CategorysViewSet, costs_category


router = DefaultRouter()
router.register('costs', CostsViewSet)
#router.register('costs/(?P<slug>\d+)/', CostsCategoryViewSet, basename='costs_category')
router.register('category', CategorysViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('costs/<int:pk>/', costs_category)
]