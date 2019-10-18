from django.contrib import admin
from .models import About, AboutType
# Register your models here.


@admin.register(AboutType)
class AboutTypeAdmin(admin.ModelAdmin):
    list_display = ("id","about_type","created_time")
    list_per_page = 10  # 每页显示10条


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id","about_type","created_time")
    list_per_page = 10  # 每页显示10条