from arminit import MoveArm
def baseclockwise():
    MoveArm(1,[0,1,0]) #Rotate base anti-clockwise
    return 'the arm has moved!!!'

def baseanticlockwise():
    MoveArm(1,[0,2,0]) #Rotate base clockwise
    return 'the arm has moved!!!'