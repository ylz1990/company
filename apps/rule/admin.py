from django.contrib import admin
from .models import RuleType, Rule
# Register your models here.


@admin.register(RuleType)
class RuleTypeAdmin(admin.ModelAdmin):
    list_display = ("id","rule_type","created_time")
    list_per_page = 10  # 每页显示10条


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("id","title","rule_type","author","read_num","created_time")
    list_per_page = 10  # 每页显示10条
