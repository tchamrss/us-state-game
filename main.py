import turtle
import pandas

FONT = ("Courier", 10, "normal")

screen = turtle.Screen()


def write_state(name, x_cor, y_cor):
    state_name = turtle.Turtle()
    state_name.hideturtle()
    state_name.penup()
    state_name.goto(x_cor, y_cor)
    state_name.write(f"{name}", align="center", font=FONT)

screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
guessed_states = []
while len(guessed_states) < 50:
    answer_user = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name ?")
    #print(answer_user)

    states = pandas.read_csv("50_states.csv")
    state_and_coordinates = states[states.state == answer_user.capitalize()]
    all_states = states.state.to_list()
    #state = state_and_coordinates.iloc[0]['state']
    #x = state_and_coordinates.iloc[0]['x']
    #y = state_and_coordinates.iloc[0]['y']
    #state_dict = state_and_coordinates.to_dict()

    if answer_user.capitalize() == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")

        break
    if state_and_coordinates.size:
        guessed_states.append(answer_user.capitalize())
        write_state(answer_user.capitalize(), int(state_and_coordinates.x), int(state_and_coordinates.y))
    else:
        print("nicht gefunden")


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

#screen.exitonclick()


