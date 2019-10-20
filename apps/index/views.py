from django.shortcuts import render
from news.models import News
# Create your views here.


def index(request):
    news = News.objects.only('id',"title","created_time").order_by("-created_time")[0:5]
    return render(request,"index/index.html",locals())



def contact(request):
    return render(request, "index/contact.html")



def page_not_found(request):
    return render(request, "handler_404.html")

def page_error(request):
    return render(request, "handler_500.html")