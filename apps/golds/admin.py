from django.contrib import admin
from .models import Golds,GoldType
# Register your models here.


@admin.register(GoldType)
class GoldTypeAdmin(admin.ModelAdmin):
    list_display = ("id","gold_type","created_time")
    list_per_page = 10  # 每页显示10条


@admin.register(Golds)
class GoldsAdmin(admin.ModelAdmin):
    list_display = ("id","title","gold_type","author","read_num","created_time")
    list_per_page = 10  # 每页显示10条

