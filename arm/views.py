from django.shortcuts import render
from django.http import HttpResponse
from arminit import MoveArm, StartArm, StopArm

def index(request):
    context = {}
    return render(request, 'arm/index.html', context)

def stop():
    StopArm() #Rotate base anti-clockwise
    return HttpResponse('the arm has moved!!!')

def baseclockwise():
    StartArm([0,1,0]) #Rotate base anti-clockwise
    return HttpResponse('the arm has moved!!!')

def baseanticlockwise():
    StartArm([0,2,0]) #Rotate base clockwise
    return HttpResponse('the arm has moved!!!')

def up():
    StartArm([64,0,0]) #Shoulder up
    return HttpResponse('the arm has moved!!!')

def down():
    StartArm([128,0,0]) #Shoulder down
    return HttpResponse('the arm has moved!!!')

def elbowup():
    StartArm([16,0,0]) #Elbow up
    return HttpResponse('the arm has moved!!!')

def elbowdown():
    StartArm([32,0,0]) #Elbow down
    return HttpResponse('the arm has moved!!!')

def wristup():
    StartArm([4,0,0]) #Wrist up
    return HttpResponse('the arm has moved!!!')

def wristdown():
    StartArm([8,0,0]) # Wrist down
    return HttpResponse('the arm has moved!!!')

def gripopen():
    StartArm([2,0,0]) #Grip open
    return HttpResponse('the arm has moved!!!')

def gripclose():
    StartArm([1,0,0]) #Grip close
    return HttpResponse('the arm has moved!!!')

def lighton():
    StartArm([0,0,1]) #Light on
    return HttpResponse('the arm has moved!!!')

def lightoff():
    StartArm([0,0,0]) #Light off
    return HttpResponse('the arm has moved!!!')