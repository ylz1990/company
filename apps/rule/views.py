from django.shortcuts import render
from .models import Rule,RuleType
from django.core.paginator import Paginator
# Create your views here.

def rule(request):
    #  黄金市场政策
    rule_all_list = Rule.objects.only("id", "title", "text").filter(rule_type=3).order_by("-created_time")
    paginator = Paginator(rule_all_list, 5)
    # 获取当前页 默认是第一页
    page_num = request.GET.get('page', 1)
    # 获取当前页上的新闻
    page_of_news = paginator.get_page(page_num)
    rules = page_of_news.object_list
    # 获取当前页码数
    currentr_page_num = page_of_news.number
    # 当前页的前两页码数和后三页的页码数显示，其余的页码数隐藏
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]
    return render(request, "rule/rule.html", locals())


def ywgz(request):
    #  业务规则
    rule_all_list = Rule.objects.only("id", "title", "text").filter(rule_type=1).order_by("-created_time")
    paginator = Paginator(rule_all_list, 5)
    # 获取当前页 默认是第一页
    page_num = request.GET.get('page', 1)
    # 获取当前页上的新闻
    page_of_news = paginator.get_page(page_num)
    rules = page_of_news.object_list
    # 获取当前页码数
    currentr_page_num = page_of_news.number
    # 当前页的前两页码数和后三页的页码数显示，其余的页码数隐藏
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]
    return render(request, "rule/ywgz.html", locals())

def qsjs(request):
    #  清算与结算
    rule_all_list = Rule.objects.only("id", "title", "text").filter(rule_type=2).order_by("-created_time")
    paginator = Paginator(rule_all_list, 5)
    # 获取当前页 默认是第一页
    page_num = request.GET.get('page', 1)
    # 获取当前页上的新闻
    page_of_news = paginator.get_page(page_num)
    rules = page_of_news.object_list
    # 获取当前页码数
    currentr_page_num = page_of_news.number
    # 当前页的前两页码数和后三页的页码数显示，其余的页码数隐藏
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]
    return render(request, "rule/qsjs.html", locals())

def jgdj(request):
    #  交割与定价
    rule_all_list = Rule.objects.only("id", "title", "text").filter(rule_type=4).order_by("-created_time")
    paginator = Paginator(rule_all_list, 5)
    # 获取当前页 默认是第一页
    page_num = request.GET.get('page', 1)
    # 获取当前页上的新闻
    page_of_news = paginator.get_page(page_num)
    rules = page_of_news.object_list
    # 获取当前页码数
    currentr_page_num = page_of_news.number
    # 当前页的前两页码数和后三页的页码数显示，其余的页码数隐藏
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]
    return render(request, "rule/jgdj.html", locals())

def fxqzl(request):
    #  反洗钱专栏
    rule_all_list = Rule.objects.only("id", "title", "text").filter(rule_type=5).order_by("-created_time")
    paginator = Paginator(rule_all_list, 5)
    # 获取当前页 默认是第一页
    page_num = request.GET.get('page', 1)
    # 获取当前页上的新闻
    page_of_news = paginator.get_page(page_num)
    rules = page_of_news.object_list
    # 获取当前页码数
    currentr_page_num = page_of_news.number
    # 当前页的前两页码数和后三页的页码数显示，其余的页码数隐藏
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]
    return render(request, "rule/fxqzl.html", locals())

def rule_d(request, rule_id):
    rule = Rule.objects.get(id=rule_id)
    rule_all = Rule.objects.all().order_by("?")[:6]
    rule.read_num += 1
    rule.save()
    # 上一篇
    previoud_new = Rule.objects.filter(created_time__lt=rule.created_time).last()
    # 下一篇
    next_new = Rule.objects.filter(created_time__gt=rule.created_time).first()
    return render(request, "rule/rule_d.html", locals())


