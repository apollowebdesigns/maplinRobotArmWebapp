from flask import Flask
from movearm import baseclockwise, baseanticlockwise, up, down, elbowup, elbowdown, wristup, wristdown, gripopen, gripclose, lighton, lightoff
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'hello world, the app has landed'

@app.route('/baseclockwise')
def baseclockwise_root():
   return baseclockwise()

@app.route('/baseanticlockwise')
def baseanticlockwise_root():
   return baseanticlockwise()

@app.route('/up')
def up_root():
   return up()

@app.route('/down')
def down_root():
   return down()

@app.route('/elbowup')
def elbowup_root():
   return elbowup()

@app.route('/elbowdown')
def elbowdown_root():
   return elbowdown()

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)