from django.shortcuts import render
from notice.models import Notice

def home(request):
    notice = Notice.objects.filter(type='notice').order_by('-updated')[:5]
    news = Notice.objects.filter(type='news').order_by('-updated')[:5]

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
