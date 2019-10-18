from django.shortcuts import render
from .models import About
# Create your views here.



def about(request):
    # 关于公司
    abouts = About.objects.filter(about_type=1)
    return render(request,"about/about.html",locals())


def culture(request):
    # 企业文化
    cultures = About.objects.filter(about_type=2)
    return render(request, "about/culture.html", locals())

def ideal(request):
    #  品牌理念
    ideals = About.objects.filter(about_type=3)
    return render(request, "about/ideal.html", locals())
