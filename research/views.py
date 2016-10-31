from django.shortcuts import render
from .models import Vision, Research


def research(request):
    vision = Vision.objects.first()
    research = Research.objects.all()

    template = 'research/research.html'
    context = {
        'vision': vision,
        'research': research,
    }

    return render(request, template, context)
