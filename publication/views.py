from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Publication
from .crawling import publication_c

def publication(request, type=None):
    publication_c()
    if type is None:
        type = 'journal'

    queryset_list = Publication.objects.filter(type=type)

    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    template = 'pub/publication.html'
    context = {
        "pub": queryset,
        "page_request_var": page_request_var,
        "type": type
    }

    return render(request, template, context)


def pub_detail(request, pub_id):
    pub = Publication.objects.get(id=pub_id)

    template = 'pub/detail.html'
    context = {
        "pub": pub
    }

    return render(request, template, context)
