from django.shortcuts import render
from django.shortcuts import render_to_response
from NineCo.models import JobsInfo,Classification


def Index(request):
    return render_to_response("index.html")


def summary(request):
    return render_to_response("summary.html")


def contact(request):
    return render(request, "contact.html")


def jobs(request):
	#jobsinfos=JobsInfo.objects.filter().order_by('dimDate')
    return render_to_response("jobs.html")