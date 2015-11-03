from django.shortcuts import render
from django.shortcuts import render_to_response
from NineCo.models import JobsInfo,Classification,GameInfo,GameClass


def Index(request):
    return render_to_response("index.html")


def summary(request):
    return render_to_response("summary.html")


def contact(request):
    return render(request, "contact.html")


def jobs(request):
    jobsinfos=JobsInfo.objects.all().order_by('-dimDate')
    classifications=Classification.objects.all()
    return render_to_response("jobs.html",{'jb':jobsinfos,'cl':classifications})

def gamelist(request):
    games=GameInfo.objects.all().order_by('-dimDate')
    return render_to_response("gamelist.html",{'gm':games})

def gamecl(request):
    games=GameInfo.objects.all().order_by('-dimDate')
    gc=GameClass.objects.all()
    return render_to_response("allgame.html",{'gm':games,'gc':gc})