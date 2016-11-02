from django.shortcuts import render
from .models import Protocol, PROTOCOL_TYPE


def protocol_list(request):
    protocol = Protocol.objects.all()
    type = PROTOCOL_TYPE

    template = 'protocol/protocol_list.html'
    context = {
        "protocol": protocol,
        "type": type,
    }

    return render(request, template, context)
