from django.shortcuts import render

# Create your views here.


def golds(request):
    return render(request,"golds/golds.html")