from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(100, 'red')
    back(100)
    right(90)
    forward(100)
    dot(100, 'light green')
    back(100)
    right(90)
    forward(100)
    dot(100, 'sky blue')
    back(100)
    right(90)
    forward(100)
    dot(100, 'sky blue')
    back(100)
    right(90)
    dot(40,'red')
    dot(20,'white')
    
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=10

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(60)
onkey(flick, 'space')
listen()
animate()
done()