from django.shortcuts import render
from .models import Protocol


def protocol_list(request):
    protocol = Protocol.objects.all()

    template = 'protocol/protocol_list.html'
    context = {
        "protocol": protocol
    }

    return render(request, template, context)
