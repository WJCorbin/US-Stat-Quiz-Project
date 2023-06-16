import turtle
import pandas
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S. State Quiz")
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
label = turtle.Turtle()
label.penup()
label.hideturtle()
guessed_states = []
answer = screen.textinput(title="Guess A State:", prompt="What is the name of a state?: ").title()
while len(guessed_states) < 50:
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in guessed_states:
        answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct:",
                                  prompt="Already Guessed!!! What is the name of another state?: ").title()
    elif answer in all_states:
        state_data = data[data.state == answer]
        label.goto(int(state_data.x), int(state_data.y))
        label.write(answer)
        guessed_states.append(answer)
        answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct:",
                                  prompt="Correct!!! What is the name of another state?: ").title()
    else:
        answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct:",
                                  prompt="Incorrect!!! What is the name of another state?: ").title()
screen.exitonclick()
