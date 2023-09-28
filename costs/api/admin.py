from django.contrib import admin
from .models import Cost, Category


class CaregoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

admin.site.register(Cost)
admin.site.register(Category)