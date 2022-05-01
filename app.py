from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__) #app initialized

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/Abh')
def Abh():
    return 'My name is Abhisek'

@app.route('/index')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)