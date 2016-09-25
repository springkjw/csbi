from django.shortcuts import render
from notice.models import Notice

def home(request):
    notice = Notice.objects.filter(type='notice')[:5]
    news = Notice.objects.filter(type='news')[:5]

    template = 'home.html'
    context = {
        'notice': notice,
        'news': news,
    }

    return render(request, template, context)


def profile(request):
    template = 'prof/profile.html'
    context = {

    }

    return render(request, template, context)


def research(request):
    template = 'research/research.html'
    context = {

    }

    return render(request, template, context)
