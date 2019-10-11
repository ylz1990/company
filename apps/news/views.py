from django.shortcuts import render
from .models import News, HeadlineNews
from django.core.paginator import Paginator
# Create your views here.


def news(request):
    # 头条新闻
    headline_news = HeadlineNews.objects.only("id","title","created_time","text", "img_url").order_by("-created_time")
    # 全部新闻
    news_all_list = News.objects.only("id","title","created_time","text").order_by("-created_time")
    # 分页  每页显示5条 全部新闻内容
    paginator = Paginator(news_all_list, 5)
    # 获取当前页 默认是第一页
    page_num = request.GET.get('page', 1)
    # 获取当前页上的新闻
    page_of_news = paginator.get_page(page_num)
    news = page_of_news.object_list
    # 获取当前页码数
    currentr_page_num = page_of_news.number
    # 当前页的前两页码数和后三页的页码数显示，其余的页码数隐藏
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]
    return render(request,"news/news.html", locals())


def new_detail(request, new_id):
    # 显示全部新闻的详情
    new = News.objects.get(id=new_id)
    # 阅读次数
    new.read_num += 1
    new.save()
    # 显示热点文章 按阅读量排行
    hot_news =  News.objects.all().order_by("-read_num")[0:5]
    return render(request,"news/news_d.html", locals())


def headline_news_detail(request, head_id):
    # 显示隐藏新闻的详情
    head = HeadlineNews.objects.get(id=head_id)
    # 阅读次数
    head.read_num += 1
    head.save()
    return render(request,"news/news_detail.html", locals())