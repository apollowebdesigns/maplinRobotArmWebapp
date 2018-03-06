"""
Times are controlled from within this file for grip
"""
duration = 0.2

from arminit import MoveArm
def baseclockwise():
    MoveArm(duration,[0,1,0]) #Rotate base anti-clockwise
    return 'the arm has moved!!!'

def baseanticlockwise():
    MoveArm(duration,[0,2,0]) #Rotate base clockwise
    return 'the arm has moved!!!'

def up():
    MoveArm(duration,[64,0,0]) #Shoulder up
    return 'the arm has moved!!!'

def down():
    MoveArm(duration,[128,0,0]) #Shoulder down
    return 'the arm has moved!!!'

def elbowup():
    MoveArm(duration,[16,0,0]) #Elbow up
    return 'the arm has moved!!!'

def elbowdown():
    MoveArm(duration,[32,0,0]) #Elbow down
    return 'the arm has moved!!!'

def wristup():
    MoveArm(duration,[4,0,0]) #Wrist up
    return 'the arm has moved!!!'

def wristdown():
    MoveArm(duration,[8,0,0]) # Wrist down
    return 'the arm has moved!!!'

def gripopen():
    MoveArm(duration,[2,0,0]) #Grip open
    return 'the arm has moved!!!'

def gripclose():
    MoveArm(duration,[1,0,0]) #Grip close
    return 'the arm has moved!!!'

def lighton():
    MoveArm(duration,[0,0,1]) #Light on
    return 'the arm has moved!!!'

def lightoff():
    MoveArm(duration,[0,0,0]) #Light off
    return 'the arm has moved!!!'