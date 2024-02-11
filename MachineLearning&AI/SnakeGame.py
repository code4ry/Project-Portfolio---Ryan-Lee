## AP Computer Science Principles Portfolio Task ##
## Snake Game ##

import turtle as trtl
import random as rand

## initializes screen and screen size
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgcolor("green")

snakeList = []

## initializes the turtle for the snake's head, the apple, and the score
snakeHead = trtl.Turtle()
snakeHead.pu()
snakeHead.speed(1)
snakeHead.color("blue")
snakeHead.shape("square")
apple = trtl.Turtle()
apple.pu()
apple.shape("square")
apple.color("red")
apple.goto(-200, 0)
goldApple = trtl.Turtle()
goldApple.pu()
goldApple.shape("square")
goldApple.color("yellow")
goldApple.goto(100, 100)
scoreWriter = trtl.Turtle()
scoreWriter.pu()
scoreWriter.color("white")
scoreWriter.hideturtle()
scoreWriter.goto(0, 250)
gameWriter = trtl.Turtle()
gameWriter.pu()
gameWriter.color("white")
gameWriter.hideturtle()
score = 0

snakeHead.direction = "left"

## function for making the snake disappear when the game ends
def snake_gone():
    snakeHead.hideturtle()
    for snake in snakeList:
        snake.hideturtle()
        snake.goto(1000,1000)
        gameWriter.write("You Lose :( Play again?", align="Center", font=("Arial", 30,"normal"))

## function for operating and increasing the score count when
def score_counter(active_apple):
    global score
    scoreWriter.clear()
    if active_apple == goldApple:
        score = score + 5
    else:
        score= score + 1
    scoreWriter.write("Score: " + str(score), align="Center", font=("Arial", 30, "normal"))
    return score

## function for randomly respawning the apple after the apple has been eaten
def relocate_apple(active_apple):
    x_coor = rand.randint(-300, 300)
    y_coor = rand.randint(-150, 150)
    active_apple.goto(x_coor, y_coor)
    active_apple.showturtle()


## function for growing the snake's body when the snake eats the apple
def snakeGrow():
    wn.tracer(True)
    snakeBody = trtl.Turtle()
    snakeBody.hideturtle()
    snakeBody.pu()
    snakeBody.shape("square")
    snakeBody.color("blue")
    snakeBody.speed(-1)
    snakeBody.goto(1000,1000)
    snakeBody.showturtle()
    snakeList.append(snakeBody)
    snakeBody.speed(0)

## function for when the snake's head touches its body
def snakeTouch(a):
    for i in range(len(snakeList)):
        if abs(a.xcor() - snakeList[i].xcor()) < 20:
            if abs(a.ycor() - snakeList[i].ycor()) < 20:
                snake_gone()
                a.direction = "stop"



## function for when the snake touches the borders of the game
def borderTouch(a):
    x_coor = a.xcor()
    y_coor = a.ycor()
    if x_coor > 390 or x_coor < -390:
        a.direction = "stop"
        snake_gone()
    elif y_coor > 290 or y_coor < -290:
        a.direction = "stop"
        snake_gone()


## function for what happens when the snake eats the apple
def apple_spawn(active_apple):
    if abs(snakeHead.xcor() - active_apple.xcor()) < 20:
        if abs(snakeHead.ycor() - active_apple.ycor()) < 20:
            snakeGrow()
            active_apple.hideturtle()
            relocate_apple(apple)
            relocate_apple(goldApple)
            active_apple.showturtle()
            score_counter(active_apple)
            wn.update()

## functions for changing the direction of the snake
def right():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"
def left():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"
def up():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"
def down():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"

## function for moving the snake depending on the direction chosen from the previous functions above
### code below offered by https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900 #####
def moveSnake(a):
    if a.direction == "right":
        a.setx(a.xcor() + 20)
    if a.direction == "left":
        a.setx(a.xcor() - 20)
    if a.direction == "up":
        a.sety(a.ycor() + 20)
    if a.direction == "down":
        a.sety(a.ycor() - 20)
####################################################################

## events that allows for user to input snake's direction
wn.listen()
wn.onkeypress(right, "Right")
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")

while True:

    ## code for moving each part of the snake's body with the head of the snake
    ### code below offered by https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900 #####
    for index in range(len(snakeList)-1, 0, -1):
        x_coor = snakeList[index-1].xcor()
        y_coor = snakeList[index-1].ycor()
        snakeList[index].goto(x_coor, y_coor)

    if len(snakeList) > 0:
        snakeList[0].goto(snakeHead.xcor(),snakeHead.ycor())
    #####################################################################

    moveSnake(snakeHead)
    apple_spawn(apple)
    apple_spawn(goldApple)
    snakeTouch(snakeHead)
    borderTouch(snakeHead)





wn.mainloop()