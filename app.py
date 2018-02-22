from flask import Flask
from movearm import move_arm
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'hello world, the app has landed'

@app.route('/move')
def move_that_arm():
   return move_arm()

if __name__ == '__main__':
   app.run()