# Maplin Robot Arm App

This app is a django app for controlling the maplin robot arm from a Raspberry Pi

python manage.py runserver 8080

### Demo Arm Commands
MoveArm(1,[0,1,0]) #Rotate base anti-clockwise
MoveArm(1,[0,2,0]) #Rotate base clockwise
MoveArm(1,[64,0,0]) #Shoulder up
MoveArm(1,[128,0,0]) #Shoulder down
MoveArm(1,[16,0,0]) #Elbow up
MoveArm(1,[32,0,0]) #Elbow down
MoveArm(1,[4,0,0]) #Wrist up
MoveArm(1,[8,0,0]) # Wrist down
MoveArm(1,[2,0,0]) #Grip open
MoveArm(1,[1,0,0]) #Grip close
MoveArm(1,[0,0,1]) #Light on
MoveArm(1,[0,0,0]) #Light off