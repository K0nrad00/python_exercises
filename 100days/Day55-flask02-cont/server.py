# THIS IS CHALLENGE FROM THE LESSON
import random
from flask import Flask

app = Flask(__name__)
# print(__name__)

GIPHY = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
NO_KITTEN = 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExajd4aGZmcHVhcmdubW5wY2I3Y3h4bGxlZXNoNWVqcWoyMzQyYjVoNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/dzH5pt95QtHPsucjof/giphy.webp'
KITTEN_FOUND = 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDJqdHV2emphYnBuYWN3cGo2OHl4bmYwaDQ2Ync1dmYwaW1nOTk0ayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/S9MgilK1rpCmCCWddy/giphy.webp'

@app.route("/")
def guess():
    return "<h1>Guess a number between 0 and 9</h1>" \
            f"<img src={GIPHY}>"

def generate_number(): #this doesn't need to be wrapped in function at all
    rand = random.randint(0,9)
    return rand

generated_number = generate_number()
# print(generated_number) #DEBUG
@app.route("/<int:user_number>")
def check(user_number):
    # user_number = input(guess())
    # user_number = int(user_number)
    if user_number == generated_number:
        return "<h1 style='color:green'>You've found me</h1>" \
               f"<img src={KITTEN_FOUND}>"
    elif user_number > generated_number:
        return "<h1 style='color:purple'>Too high, try again</h1>" \
                f"<img src={NO_KITTEN}>"
    else:
        return "<h1 style='color:red'>Too low, try again</h1>" \
                f"<img src={NO_KITTEN}>"


if __name__ == "__main__":
    app.run(debug=True)