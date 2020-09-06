import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#Set screen
wd = turtle.Screen()
wd.title("Snake game")
wd.bgcolor("black")
wd.setup(width=800, height=800)
wd.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

#Food
food = turtle.Turtle()
colors = random.choice(['red','white','purple'])
shapes = random.choice(['square','triangle','circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

segments=[]
pen = turtle.Turtle()
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0 High score: 0",align="center",font=("arial",26,"bold"))

def goup():
    if head.direction != "down":
        head.direction = "up"
def godown():        
    if head.direction != "up":
        head.direction = "down"
def goright():        
    if head.direction != "left":
        head.direction = "right"
def goleft():       
    if head.direction != "right":
        head.direction = "left"        

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wd.listen()
wd.onkeypress(goup, "w")
wd.onkeypress(godown, "s")
wd.onkeypress(goleft, "a")
wd.onkeypress(goright, "d")

#Main game loop

while True:
    wd.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        colors = random.choice(['red', 'green', 'white', 'purple'])
        shapes = random.choice(['square', 'triangle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High score : {} ".format(score, high_score), align="center", font=("arial", 26, "bold"))
    #Check collision with the food    
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High score: {}".format(score, high_score), align="center", font=("arial", 26, "bold"))

    for index in range(len(segments)-1,0,-1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            colors = random.choice(['red','green','white','purple'])
            shapes = random.choice(['square','triangle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High score : {} ".format(score,high_score),align="center",font=("arial",26,"bold"))
    time.sleep(delay)

wd.mainloop() 