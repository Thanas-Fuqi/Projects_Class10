
import turtle 
import math

screen = turtle.Screen()
turtle.bgpic("human.png")

def draw(rad, n):
  for i in range(2):
    n.circle(rad,90)
    n.circle(rad//2,90)

def funky(x):
  y = math.sqrt(160_000-x**2)
  return y

colors = ["aqua", "black", "blue", "pink", "red",
          "green", "orange", "grey", "yellow", "purple",
          "lime", "bisque4", "blueviolet", "chocolate", "crimson"]

turtles = []
for i in range(7):
  tur = str(i)
  
  tur = turtle.Turtle()
  tur.speed(0)
  tur.penup()
  tur.shape("circle")
  tur.color(colors[i])
  tur.shapesize(2)
  
  tur.goto(-400+(100*(i+1)), funky(-400+(100*(i+1))))
  
  tur.right(135+(i*15))
  tur.speed(10)
  #tur.pendown()

  turtles.append(tur)

for i in range(8):
  tur = str(i+7)
  
  tur = turtle.Turtle()
  tur.speed(0)
  tur.penup()
  tur.shape("circle")
  tur.color(colors[i+7])
  tur.shapesize(2)
  
  tur.goto(-400+(100*(i+1)), -(funky(-400+ (100*(i+1)))))
  
  tur.left(10*(i+1))
  tur.speed(10)
  #tur.pendown()

  turtles.append(tur)

run = True
tr = 0

while run:
    
  if tr == 7:
    tr = -1

  if tr == -9:
    tr *= 0
    
  if tr < 1 and tr!=0:
    bl = turtles[tr]
    draw(500, bl)
    tr -= 1

  elif tr >= 1 or tr==0:
    bl = turtles[tr]
    draw(500, bl)

    tr += 1
