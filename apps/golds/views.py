from django.shortcuts import render
from .models import Golds
from django.core.paginator import Paginator
# Create your views here.


def golds(request):
    # 黄金TD资讯
    golds_all_list = Golds.objects.only("id","title","created_time","text").filter(gold_type=1).order_by("-created_time")
    paginator = Paginator(golds_all_list, 5)
    # 获取当前页 默认是第一页
    page_num = request.GET.get('page', 1)
    # 获取当前页上的新闻
    page_of_news = paginator.get_page(page_num)
    golds = page_of_news.object_list
    # 获取当前页码数
    currentr_page_num = page_of_news.number
    # 当前页的前两页码数和后三页的页码数显示，其余的页码数隐藏
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]
    return render(request,"golds/golds.html",locals())


def golds_tz(request):
    # 黄金投资
    golds_all_list = Golds.objects.only("id","title","created_time","text").filter(gold_type=2).order_by("-created_time")
    paginator = Paginator(golds_all_list, 5)
    # 获取当前页 默认是第一页
    page_num = request.GET.get('page', 1)
    # 获取当前页上的新闻
    page_of_news = paginator.get_page(page_num)
    golds = page_of_news.object_list
    # 获取当前页码数
    currentr_page_num = page_of_news.number
    # 当前页的前两页码数和后三页的页码数显示，其余的页码数隐藏
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]
    return render(request,"golds/golds_tz.html",locals())


def golds_gd(request):
    # 机构观点
    golds_all_list = Golds.objects.only("id","title","created_time","text").filter(gold_type=3).order_by("-created_time")
    paginator = Paginator(golds_all_list, 5)
    # 获取当前页 默认是第一页
    page_num = request.GET.get('page', 1)
    # 获取当前页上的新闻
    page_of_news = paginator.get_page(page_num)
    golds = page_of_news.object_list
    # 获取当前页码数
    currentr_page_num = page_of_news.number
    # 当前页的前两页码数和后三页的页码数显示，其余的页码数隐藏
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]
    return render(request,"golds/golds_gd.html",locals())

def golds_fx(request):
    # 机构分析
    golds_all_list = Golds.objects.only("id","title","created_time","text").filter(gold_type=4).order_by("-created_time")
    paginator = Paginator(golds_all_list, 5)
    # 获取当前页 默认是第一页
    page_num = request.GET.get('page', 1)
    # 获取当前页上的新闻
    page_of_news = paginator.get_page(page_num)
    golds = page_of_news.object_list
    # 获取当前页码数
    currentr_page_num = page_of_news.number
    # 当前页的前两页码数和后三页的页码数显示，其余的页码数隐藏
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]
    return render(request,"golds/golds_fx.html",locals())

def golds_d(request, golds_id):
    gold = Golds.objects.get(id=golds_id)
    gold_all = Golds.objects.all().order_by("-read_num")[:6]
    gold.read_num += 1
    gold.save()
    # 上一篇
    previoud_new = Golds.objects.filter(created_time__lt=gold.created_time).last()
    # 下一篇
    next_new = Golds.objects.filter(created_time__gt=gold.created_time).first()
    return render(request,"golds/golds_d.html",locals())
