from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CostsViewSet, CategorysViewSet, CostsCategoryViewSet


router = DefaultRouter()
router.register('costs', CostsViewSet)
router.register('category', CategorysViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('costs-category/<str:category_slug>/', CostsCategoryViewSet.as_view({'get': 'retrieve'}), name='costs-category-detail')
]