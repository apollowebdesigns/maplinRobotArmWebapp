import os
location = '/home/pi/maplinRobotArmWebapp/'
bashCommand = 'sudo python3 ' + location + 'manage.py runserver 0:8000'
os.system(bashCommand)