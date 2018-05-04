# Maplin Robot Arm App

~~This app is a django app for controlling the maplin robot arm from a Raspberry Pi~~

~~python manage.py runserver 8080~~

python manage.py runserver 0:8000

make life easy and install the shell script

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

### Useful urls

https://www.wikihow.com/Use-a-USB-Robotic-Arm-with-a-Raspberry-Pi-(Maplin)

note, one of the ids are wrong so for python use lsusb command to find the write id

### Tests

#### UI testing

Protractor is currently being used for UI testing in the project

For Python Selenium, webdriver needs to be started and you need to have chromedriver to interact with chrome.

pip install behave for cucumber language for python

## Useful urls

Maplin arm on mobile phone

http://172.20.10.8/arm/