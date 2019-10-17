from django.contrib import admin
from .models import Recruit
# Register your models here.


@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    list_display = ("id","title","author","created_time")
    list_per_page = 10  # 每页显示10条

