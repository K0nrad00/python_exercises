from flask import Flask
# export FLASK_APP=hello.py
# 'flask run' - to run the server

app = Flask(__name__)

print(__name__)

@app.route("/") #Decorators explenation code: https://replit.com/@appbrewery/python-decorators#main.py
# you can visualize this here: https://pythontutor.com/visualize.html#mode=edit
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__": # this is to replace 'flask run'
    app.run()