from flask import Flask
# export FLASK_APP=main.py or FLASK_APP=development (for debug)
# flask run

app = Flask(__name__)


# Decorator 1
def make_bold(function): #add <b></b> html tags
    def wrap():
        result = f"<b>{function()}</b>"
        return result
    return wrap

# Decorator 2
def make_emphasis(func):
    def wrapper():
        res = f"<em>{func()}</em>"
        return res
    return wrapper

# Decorator 3
def make_underline(f):
    def wrap():
        r = f"<u>{f()}</u>"
        return r
    return wrap



@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>Paragraph</p>"
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmxnazZiMXc2dzdjeHNnOXB4dWlicjRoZGpsdG56NzlxcjhrdGxwbCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oriO0OEd9QIDdllqo/giphy.gif' width=400>")

@app.route("/bye")
@make_bold
@make_emphasis #<em>
@make_underline #<u>
def bye():
    return "Bye!"

@app.route("/<name>/<int:number>") #<converter: https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules
def greet(name, number):
    return f"Hello there {name}! You are {number} year old" #http://127.0.0.1:5000/Tom/37

if __name__ == "__main__": # this is to replace 'flask run'
    app.run(debug=True) #instead of export FLASK_APP=development