import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_list = []

while len(guessed_list) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_list)}/50 States guessed",
                                     prompt="Whats another state's name").title()
    print(answer_states)

    if answer_states == "Exit":
        missing_states = []
        for state in  all_states:
            if state not in guessed_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_states in all_states:
        guessed_list.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = data[data.state == answer_states]
        t.goto(int(states_data.x), int(states_data.y))
        t.write(answer_states)





#Code below is to get x,y co-ordinates of a image
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()




