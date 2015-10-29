from django.shortcuts import render
from django.shortcuts import render_to_response


def Index(request):
    return render_to_response("index.html")
