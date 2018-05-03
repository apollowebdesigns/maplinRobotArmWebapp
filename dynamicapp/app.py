from flask import Flask, request, Response, render_template
import movearm
from movearm import start_baseclockwise, stop, baseclockwise, baseanticlockwise, up, down, elbowup, elbowdown, wristup, wristdown, gripopen, gripclose, lighton, lightoff
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/stop')
def stop_root():
   return stop()

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

@app.route('/wristup')
def wristup_root():
   return wristup()

@app.route('/wristdown')
def wristdown_root():
   return wristdown()

@app.route('/gripopen')
def gripopen_root():
   return gripopen()

@app.route('/gripclose')
def gripclose_root():
   return gripclose()

@app.route('/lighton')
def lighton_root():
   return lighton()

@app.route('/lightoff')
def lightoff_root():
   return lightoff()

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)