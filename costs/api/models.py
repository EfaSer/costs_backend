from django.db import models

class Cost(models.Model):
  """Модель расходов"""
  description = models.TextField(max_length=255, verbose_name="Описание")
  amount = models.FloatField(max_length=255, verbose_name="Цена")
  date = models.TextField(verbose_name="Дата")
  category = models.ForeignKey("Category", on_delete=models.PROTECT, related_name='category')
  class Meta:
    verbose_name_plural = "Расходы"


class Category(models.Model):
  """Модель категорий"""
  name = models.CharField(max_length=30, verbose_name="Категория")
  slug = models.SlugField(max_length=30, unique=True, verbose_name="URL")

  class Meta:
    verbose_name_plural = "Расходы"

  def __str__(self) -> str:
    return self.name