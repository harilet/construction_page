from flask import *
import json

app = Flask(__name__)

global date
@app.route('/dashbord',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      value=result["pass"]
      if value=="hari":
          return render_template("dash.html")
      else:
          return("Wrrong password")

@app.route('/uptime',methods = ['POST', 'GET'])
def updatedate():
   global date
   if request.method == 'POST':
      result = request.form
      date=result["update"]
      return "Done"
      

@app.route('/theawsomepage')
def notup():
    global date
    return render_template("const.html",data=date)

@app.route('/')
def main():
   return render_template("login.html")

app.run(debug = True)