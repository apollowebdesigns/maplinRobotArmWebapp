from flask import Flask
from movearm import move_arm
app = Flask(__name__)

@app.route('/')
def hello_world():
   return move_arm()

if __name__ == '__main__':
   app.run()