from django.shortcuts import render
from django.http import HttpResponse
from arminit import MoveArm

def index(request):
    context = {}
    return render(request, 'arm/index.html', context)

def left(request):
    MoveArm(1,[0,1,0]) #Rotate base anti-clockwise
    return HttpResponse('the arm has moved!!!')

def right(request):
    MoveArm(1,[0,2,0]) #Rotate base clockwise
    return HttpResponse('the arm has moved!!!')

def up(request):
    MoveArm(1,[64,0,0]) #Shoulder up
    return HttpResponse('the arm has moved!!!')

def down(request):
    MoveArm(1,[128,0,0]) #Shoulder down
    return HttpResponse('the arm has moved!!!')

def elbowup(request):
    MoveArm(1,[16,0,0]) #Elbow up
    return HttpResponse('the arm has moved!!!')

def elbowdown(request):
    MoveArm(1,[32,0,0]) #Elbow down
    return HttpResponse('the arm has moved!!!')

def wristup(request):
    MoveArm(1,[4,0,0]) #Wrist up
    return HttpResponse('the arm has moved!!!')

def wristdown(request):
    MoveArm(1,[8,0,0]) # Wrist down
    return HttpResponse('the arm has moved!!!')

def gripopen(request):
    MoveArm(1,[2,0,0]) #Grip open
    return HttpResponse('the arm has moved!!!')

def gripclose(request):
    MoveArm(1,[1,0,0]) #Grip close
    return HttpResponse('the arm has moved!!!')

def lighton(request):
    MoveArm(1,[0,0,1]) #Light on
    return HttpResponse('the arm has moved!!!')

def lightoff(request):
    MoveArm(1,[0,0,0]) #Light off
    return HttpResponse('the arm has moved!!!')