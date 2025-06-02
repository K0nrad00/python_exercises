import pandas

import turtle

screen = turtle.Screen()
screen.title("US states game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data.state) # DEBUG

keep_guessing = True
correct_guesses = []
# correct_guesses = [ 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
# 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
# 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire'
# , 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
# 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
# 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'] # TEST/DEBUG
score = 0
states = data.state.to_list()
# print(data.state.to_list())

while keep_guessing:
    answer_state = screen.textinput(title=f"{score}/50: Guess the state", prompt="What's the state name?").title()
    if answer_state in states:
        # find coordinates of the correct guess
        row = data[data.state == answer_state]
        # print(row) # DEBUG
        # x_axis = int(row.x)
        x_axis = row.x.item() # https://pandas.pydata.org/docs/reference/api/pandas.Series.item.html
        # y_axis = int(row.y)
        y_axis = row.y.item()
        state = turtle.Turtle("blank")
        state.penup()
        state.goto(x_axis, y_axis)
        state.write(answer_state, font=("Arial", 10, "normal"))
        correct_guesses.append(answer_state)
        score += 1
    if len(correct_guesses) > 49:
        keep_guessing = False
        final_score_info = turtle.Turtle("blank")
        final_score_info.penup()
        final_score_info.write(f"You've guesses {score}/{len(correct_guesses)} state - congrats", align="left", font=("Arial", 30, "normal"))
    if answer_state.title() == "Exit":
        keep_guessing = False
        # generate csv file with states that were not guessed
        missed_states = [state for state in states if state not in correct_guesses]
        # print(missed_states) # DEBUG
        table = pandas.DataFrame({"missed states" : missed_states})
        table.to_csv("Missed_guesses.csv")


screen.exitonclick()