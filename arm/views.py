from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'arm/index.html', context)

def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")