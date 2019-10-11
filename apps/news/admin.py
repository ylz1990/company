from django.contrib import admin
from .models import News, HeadlineNews
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id","title","author","read_num","created_time")
    list_per_page = 10  # 每页显示10条


@admin.register(HeadlineNews)
class HeadlineNewsAdmin(admin.ModelAdmin):
    list_display = ("id","title","author","read_num","created_time")
    list_per_page = 10  # 每页显示10条