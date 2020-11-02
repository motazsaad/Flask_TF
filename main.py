#import random 

# step 1: import Flask 
from flask import Flask, render_template

# step 2: define Flask app 
# app = Flask("My Flask App")
app = Flask(__name__)


# step 3: define pages 

@app.route('/')
def home():
  return '<h1> Hello from Flask </h1>'

@app.route('/help')
def help():
  return '<h1> Hello from help page </h1>'
  
  
@app.route('/welcome/<name>')
def welcome(name):
  return render_template('welcome.html', name=name)


# step 4: run app 
if __name__ == "__main__":  
  app.run(debug=True)




