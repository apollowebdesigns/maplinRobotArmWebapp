from arminit import MoveArm
def baseclockwise():
    MoveArm(1,[0,1,0]) #Rotate base anti-clockwise
    return 'the arm has moved!!!'

def baseanticlockwise():
    MoveArm(1,[0,2,0]) #Rotate base clockwise
    return 'the arm has moved!!!'

def up():
    MoveArm(1,[64,0,0]) #Shoulder up
    return 'the arm has moved!!!'

def down():
    MoveArm(1,[128,0,0]) #Shoulder down
    return 'the arm has moved!!!'

def elbowup():
    MoveArm(1,[16,0,0]) #Elbow up
    return 'the arm has moved!!!'

def elbowdown():
    MoveArm(1,[32,0,0]) #Elbow down
    return 'the arm has moved!!!'

def wristup():
    MoveArm(1,[4,0,0]) #Wrist up
    return 'the arm has moved!!!'

def wristdown():
    MoveArm(1,[8,0,0]) # Wrist down
    return 'the arm has moved!!!'

def gripopen():
    MoveArm(1,[2,0,0]) #Grip open
    return 'the arm has moved!!!'

def gripclose():
    MoveArm(1,[1,0,0]) #Grip close
    return 'the arm has moved!!!'

def lighton():
    MoveArm(1,[0,0,1]) #Light on
    return 'the arm has moved!!!'

def lightoff():
    MoveArm(1,[0,0,0]) #Light off
    return 'the arm has moved!!!'