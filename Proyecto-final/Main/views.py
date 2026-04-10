from django.shortcuts import render

def index(request):
    return render(request, "Main/index.html")

from django.http import HttpResponse

def test(request):
    return HttpResponse("OK")