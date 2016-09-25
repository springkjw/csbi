from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Notice


def list(request, type=None):
    if type is None:
        type = 'notice'

    queryset_list = Notice.objects.filter(type=type).order_by('-created')

    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    template = 'notice/list.html'
    context = {
        'notice': queryset,
        "page_request_var": page_request_var,
        "type": type
    }

    return render(request, template, context)


def notice_detail(request, notice_id):
    notice = Notice.objects.get(id=notice_id)

    template = 'notice/detail.html'
    context = {
        'notice': notice
    }

    return render(request, template, context)
