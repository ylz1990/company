from django.shortcuts import render,render_to_response
from news.models import News
# Create your views here.


def index(request):
    news = News.objects.only('id',"title","created_time").order_by("-created_time")[0:5]
    return render(request,"index/index.html",locals())



def contact(request):
    return render(request, "index/contact.html")



def page_not_found(request,**kwargs):
    response = render_to_response("handler_404.html",{})
    response.status_code = 404
    return response

def page_error(request):
    return render(request, "handler_500.html")