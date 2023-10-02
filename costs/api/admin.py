from django.contrib import admin
from .models import Cost, Category


class CostAdmin(admin.ModelAdmin):
  search_fields = ("description__startswith", )
  list_display = ("id", "description", "category",)
  list_filter = ("category",)

class CategoryAdmin(admin.ModelAdmin):
  search_fields = ("name__startwith",)
  list_display = ("name", "slug")
  list_filter = ("name",)


admin.site.register(Cost, CostAdmin)
admin.site.register(Category, CategoryAdmin)

