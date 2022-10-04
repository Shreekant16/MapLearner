from turtle import Turtle, Screen
import turtle
import pandas
screen = Screen()
# This function is used to get the co-ordinates as per the turtle window
# def home(x,y):
#     print(x,y)
# screen.onscreenclick(home)

image = "map.png"
screen.bgpic(picname=image)
data = pandas.read_csv('data.csv')
states = data.state.to_list()
end = False
score = 0
while not end:
    user = turtle.textinput(title="STATE NAME", prompt="Write the state name : ")
    if user == 'off':
        print(f"{score}/29")
        end = True
    elif user in states:
        score += 1
        state_data = data[data.state == user]
        shree = Turtle()
        shree.penup()
        shree.goto(int(state_data.x), int(state_data.y))
        shree.write(user)
        shree.hideturtle()


screen.mainloop()
