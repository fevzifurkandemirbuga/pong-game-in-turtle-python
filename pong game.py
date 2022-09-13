import turtle
import joystick_class
import ball_class
from scoreBoard_pinpon import ScoreBoard

window = turtle.Screen()
window.setup(800, 600)
window.bgcolor("black")

r_kol = joystick_class.Paddle((370, 0))
l_kol = joystick_class.Paddle((-370, 0))

window.listen()
window.onkey(r_kol.go_up, "Up")
window.onkey(r_kol.go_down, "Down")
window.onkey(l_kol.go_up, "w")
window.onkey(l_kol.go_down, "s")

ball = ball_class.Ball()

l_score = 0
r_score = 0
scoreBoard = ScoreBoard()
collision = 0
while True:
    ball.forward(10)

 #******************* collision paddle********************
    if ball.xcor() >= 350 and ball.distance(r_kol) <= 50:
        collision += 1
        ball.speed(0)

        if 90 > ball.heading() > 0:
            angle = ball.heading()
            angle = angle % 90
            ball.setheading(angle + 90)
        elif 360 > ball.heading() > 270:
            angle = ball.heading()
            angle = angle % 90
            ball.setheading(angle + 180)
        ball.speed(1 + (collision * 0.2))

    if ball.xcor() <= -350 and ball.distance(l_kol) <= 50:
        collision += 1
        ball.speed(0)
        if 180 > ball.heading() > 90:
            angle = ball.heading()
            angle = angle % 90
            ball.setheading(angle)
        elif 270 > ball.heading() > 180:
            angle = ball.heading()
            angle = angle % 90
            ball.setheading(angle + 270)
        ball.speed(1 + (collision * 0.2))

#******************bounce off the wall********************
    if ball.ycor() >= 280:
        ball.speed(0)
        if 180 > ball.heading() > 90:
            angle = ball.heading()
            angle = angle % 90
            ball.setheading(angle + 180)
        elif 90 > ball.heading() > 0:
            angle = ball.heading()
            angle = angle % 90
            ball.setheading(angle + 270)
        ball.speed(1 + (collision * 0.2))

    elif ball.ycor() <= -280:
        ball.speed(0)
        if 270 > ball.heading() > 180:
            angle = ball.heading()
            angle = angle % 90
            ball.setheading(180 - angle)
        elif 360 > ball.heading() > 270:
            angle = ball.heading()
            angle = angle % 90
            ball.setheading(angle)
        ball.speed(1 + (collision * 0.2))

#********************** get score*********************************
    if abs(ball.xcor()) > 400:
        if ball.xcor() > 0:
            l_score += 1
            ball.setheading(210)
        else:
            r_score += 1
            ball.setheading(30)
        collision = 0
        scoreBoard.update(l_score, r_score)
        ball.speed(0)
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        ball.speed(1)
        ball.setheading(210)
