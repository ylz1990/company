from django.shortcuts import render
from .models import Recruit
from django.core.paginator import Paginator
# Create your views here.


def recruit(request):
    positions_all_list = Recruit.objects.all()
    paginator = Paginator(positions_all_list, 4)
    page_num = request.GET.get('page', 1)
    page_of_news = paginator.get_page(page_num)
    positions = page_of_news.object_list
    currentr_page_num = page_of_news.number
    page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                  0 < x <= paginator.num_pages]

    return render(request,"recruit/recruit.html",locals())


def recruit_d(request, recruit_id):
    position = Recruit.objects.get(id = recruit_id)
    return render(request, "recruit/recruit_d.html", locals())