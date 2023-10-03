from rest_framework import serializers
from .models import Cost, Category


class CreateCostSerializer(serializers.ModelSerializer):
  category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

  class Meta:
    model = Cost
    fields = '__all__'


class ListCostSerializer(serializers.ModelSerializer):
  category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

  class Meta:
    model = Cost
    fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = '__all__'