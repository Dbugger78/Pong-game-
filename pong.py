import turtle
import random

# Window set-up
screen = turtle.Screen()
screen.title("TURTLE")
screen.setup(width=595, height=595)
screen.tracer(0)

score_1 = 0
score_2 = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 250)

def update_score():
    pen.clear()
    pen.write(f"{score_2}                     {score_1}", align="center", font=("Arial", 24, "bold"))

# Turtle setup
t = turtle.Turtle()
t.penup()
t.speed(3)
t.shape("square")
t.shapesize(stretch_wid=1, stretch_len=4)

p2 = turtle.Turtle()
p2.shape("square")
p2.shapesize(stretch_wid=1, stretch_len=4)
p2.penup()
p2.speed(3)


ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.shapesize(0.5)

line = turtle.Turtle()

# Drawing the middle line so it actually works
line.penup()
line.hideturtle()
line.goto(0, 280)
line.setheading(270)
for _ in range(15):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

LEFT = -275
RIGHT = 280
TOP = 250
BOTTOM = -245


t.setposition(x = 275 , y = 0)
t.setheading(90)

p2.setposition(x = -282 , y = 0)
p2.setheading(90)

# Initial display
update_score()


# tracking key status (down/up)
right = {"Right": False}
left = {"Left": False}
up = {"Up": False}
down = {"Down": False}

# asighning boolen vlaues to if the key is (down/up)
def up_press():
    up["Up"] = True

def up_release():  
    up["Up"] = False

def press_down():
    down["Down"] = True

def release_down():  
    down["Down"] = False
    
def press_left():
    left["Left"] = True

def release_left():
    left["Left"] = False

def press_right():
    right["Right"] = True

def release_right():
    right["Right"] = False

#if two keys are pressed at the same time
def move_turtle_two_directions():
    x, y = t.xcor(), t.ycor()
    
    if right["Right"] == True and up["Up"] == True and x < RIGHT and y < TOP:
        t.setheading(45)
        t.forward(4)

    if right["Right"] == True and down["Down"] == True and x < RIGHT and y > BOTTOM:
        t.setheading(315)
        t.forward(4)

    if left["Left"] == True and up["Up"] == True and x > LEFT and y < TOP:
        t.setheading(135)
        t.forward(4)

    if left["Left"] == True and down["Down"] == True and x > LEFT and y > BOTTOM:
        t.setheading(225)
        t.forward(4)

    screen.update()
    screen.ontimer(move_turtle_two_directions, 8)

#movement if its single direction

def move_turtle_one_direction():
    x, y = t.xcor(), t.ycor()

    if up["Up"]:
        if y < TOP:
            t.setheading(90)
            t.forward(8)

    if down["Down"]:
        if y > BOTTOM:
            t.setheading(270)
            t.forward(8)

    screen.update()
    screen.ontimer(move_turtle_one_direction, 8)

# keybindings

screen.listen()

screen.onkeypress(press_right, "Right")
screen.onkeyrelease(release_right, "Right")

screen.onkeypress(press_left, "Left")
screen.onkeyrelease(release_left, "Left")

screen.onkeypress(up_press, "Up")
screen.onkeyrelease(up_release, "Up")

screen.onkeypress(press_down, "Down")
screen.onkeyrelease(release_down, "Down")

#code for player 2

w_key = {"w" : False}
d_key = {"d" : False}
s_key = {"s" : False}
a_key = {"a" : False}

def w_press():
    w_key["w"] = True

def w_release():  
    w_key["w"] = False

def press_d():
    d_key["d"] = True

def release_d():  
    d_key["d"] = False
    
def press_s():
    s_key["s"] = True

def release_s():
    s_key["s"] = False

def press_a():
    a_key["a"] = True

def release_a():
    a_key["a"] = False

def move_p2_two_directions():
    x, y = p2.xcor(), p2.ycor()
    
    if w_key["w"] == True and d_key["d"] == True and x < RIGHT and y < TOP:
        p2.setheading(45)
        p2.forward(4)

    if w_key["w"] == True and a_key["a"] == True and x > LEFT and y < TOP:
        p2.setheading(135)
        p2.forward(4)

    if s_key["s"] == True and d_key["d"] == True and x < RIGHT and y > BOTTOM:
        p2.setheading(315)
        p2.forward(4)

    if s_key["s"] == True and a_key["a"] == True and x > LEFT and y > BOTTOM:
        p2.setheading(225)
        p2.forward(4)

    screen.update()
    screen.ontimer(move_p2_two_directions, 8)

def move_p2_one_direction():
    x, y = p2.xcor(), p2.ycor()

    if w_key["w"]:
        if y < TOP:
            p2.setheading(90)
            p2.forward(8)

    if s_key["s"]:
        if y > BOTTOM:
            p2.setheading(270)
            p2.forward(8)

    #if a_key["a"]:
        #if x > LEFT:
            #p2.setheading(180)
            #p2.forward(8)

    #if d_key["d"]:
        #if x < RIGHT:
            #p2.setheading(0)
            #p2.forward(8)

    screen.update()
    screen.ontimer(move_p2_one_direction, 8)

screen.onkeypress(w_press, "w")
screen.onkeyrelease(w_release, "w")

screen.onkeypress(press_a, "a")
screen.onkeyrelease(release_a, "a")

screen.onkeypress(press_s, "s")
screen.onkeyrelease(release_s, "s")

screen.onkeypress(press_d, "d")
screen.onkeyrelease(release_d, "d")


#ball physics
ball.dx = 4
ball.dy = 4

def move_ball():
    global score_1, score_2
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall Bouncing
    if ball.ycor() > TOP or ball.ycor() < BOTTOM:
        ball.dy *= -1   

    # Paddle Bouncing (Checked BEFORE walls)
    if (ball.xcor() > 260 and ball.distance(t) < 40) or (ball.xcor() < -260 and ball.distance(p2) < 40):
        ball.dx *= -1
        # Slight randomness to avoid perfect loops
        ball.dx += random.uniform(-0.8, 0.1)
        ball.dy += random.uniform(-0.2, 0.8)
    
    # Boundary Scoring
    elif ball.xcor() > RIGHT:
        score_2 += 1
        update_score()
        ball.goto(0, 0)
        ball.dx = -5
        ball.dy = 5

    elif ball.xcor() < LEFT:
        score_1 += 1
        update_score()
        ball.goto(0, 0)
        ball.dx = 5
        ball.dy = 5

    screen.update()
    screen.ontimer(move_ball, 10)

# Start Loops
move_turtle_one_direction()
move_p2_one_direction()
move_ball()

screen.mainloop()