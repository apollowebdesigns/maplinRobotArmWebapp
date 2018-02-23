from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'arm/index.html', context)