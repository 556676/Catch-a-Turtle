# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
fill_color = "blue"
shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000
timer_up = False
colors = ["yellow","red","blue","purple","green"]
sizes = [1,2,3,4,5]

#-----initialize turtle-----
painter = trtl.Turtle()
painter.shape(shape)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-375,290)

counter = trtl.Turtle()


#-----game functions--------
def change_size():
    painter.shapesize(rand.choice(sizes))

def change_color():
    painter.fillcolor(rand.choice(colors))
    painter.stamp()

def painter_clicked(x,y):
    if timer > 0:
        update_score()
        change_position()
        change_color()
        change_size()
    else:
        painter.hideturtle()

def countdown():
    counter.hideturtle()
    global timer, timer_up
    counter.clear()
    counter.penup()
    counter.goto(-50,290)
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def update_score():
    global score 
    score += 1
    score_writer.clear()
    score_writer.write(score,font=font_setup)

def change_position():
    new_xpos = rand.randint(-300,300)
    new_ypos = rand.randint(-300,300)
    painter.penup() 
    painter.goto(new_xpos,new_ypos)

#-----events----------------
wn = trtl.Screen()
wn.bgcolor("orange")
painter.onclick(painter_clicked)
wn.ontimer(countdown,counter_interval)
wn.mainloop()
