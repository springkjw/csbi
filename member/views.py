from django.shortcuts import render
from .models import Member

def member(request):
    research_prof = Member.objects.filter(type='Research Professor')
    post_doc = Member.objects.filter(type='Post Doctoral Fellow')
    phd = Member.objects.filter(type='Ph.D. Candidate')
    master = Member.objects.filter(type='Master Candidate')
    staff = Member.objects.filter(type='Staff')
    alumni = Member.objects.filter(type='Alumni')

    template = 'member/member.html'
    context = {
        "prof" : research_prof,
        "post_doc": post_doc,
        "phd": phd,
        "master": master,
        "staff": staff,
        "alumni": alumni
    }

    return render(request, template, context)
