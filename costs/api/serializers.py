from rest_framework import serializers
from .models import Cost, Category


class CostSerializer(serializers.ModelSerializer):
  category = serializers.StringRelatedField()

  class Meta:
    model = Cost
    fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'