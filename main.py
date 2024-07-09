import turtle
import pandas as pd
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv('50_states.csv')

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()


message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(-150, 0)

no_of_states_guessed = 0
guessed_states = []

while no_of_states_guessed <= 50:

    state_guess = turtle.textinput(title=f"{no_of_states_guessed}/50 States Correct",
                                   prompt="What's another state's name?").title()

    if state_guess not in guessed_states:
        if states_data["state"].str.contains(state_guess).any():
            guessed_states.append(state_guess)
            no_of_states_guessed += 1
            state_data = states_data[states_data["state"] == state_guess].iloc[0]
            text_turtle.goto(int(state_data["x"]), int(state_data["y"]))
            text_turtle.write(state_guess)
        else:
            message_turtle.clear()
            message_turtle.write("State is not correct.", align="center", font=("Arial", 16, "normal"))
            time.sleep(1)
            message_turtle.clear()
    else:
        message_turtle.clear()
        message_turtle.write("State already guessed.", align="center", font=("Arial", 16, "normal"))
        time.sleep(1)
        message_turtle.clear()

    if state_guess == "Exit":
        break



unguessed_states = states_data[~states_data["state"].isin(guessed_states)]
unguessed_states.to_csv('unguessed_states.csv', index=False)