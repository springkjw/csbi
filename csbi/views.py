from django.shortcuts import render


def home(request):
    template = 'home.html'
    context = {

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
