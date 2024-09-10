
#code for the inputs 
targets  = input("How many targets do you want to have in the game?  ")
targets = int(targets)
#----------------------------------------------------------------------
Size = input("What score you want to be the high_score  ")
Size = int(Size)
#----------------------------------------------------------------------
Name1 = input("What's gone be the name for the RED player?  ")
Name2 = input("What's gone be the name for the PURPLE player?  ") 
#----------------------------------------------------------------------
theme = input("Do you want dark or light mode? ")
theme = theme.lower()

#Beginning code
import turtle
import random

#Other callings
screen = turtle.Screen()
if theme == "dark":
  turtle.bgcolor("black")
screen.title("AGAR.IO")
turtle.colormode(255)

#Variables
hei = 260
wei = 460
#------------
counter_1 = 1
counter_2 = 1
#------------
tun = []
screen.setup(wei*2+120, hei*2+200)
#----------------------------------
style = ('Courier', 25, 'italic')
style2p = ('Courier', 90, 'italic')

#Calling the used turtles
boxer = turtle.Turtle()
boxer.width(10)
if theme == "dark":
  boxer.color("white")
#-----------------------
Writer = turtle.Turtle()
if theme == "dark":
  Writer.color("white")
Writer.hideturtle()
#-----------------------
player = turtle.Turtle()
player.penup()
player.color("red")
player.shape("circle")
player.speed(0)
#------------------------
player2 = turtle.Turtle()
player2.penup()
player2.color("purple")
player2.shape("circle")
player2.speed(0)
#------------------------
points1 = turtle.Turtle()
points1.speed(0)
points1.penup()
points1.hideturtle()
points1.goto(500, 310)
#------------------------
points2 = turtle.Turtle()
points2.speed(0)
points2.penup()
points2.hideturtle()
points2.goto(-500, 310)

#Begining key function  
def PressT():
  global wei, hei
  #---------------------------
  for i in range(targets):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    #-------------------------
    t = turtle.Turtle()
    t.shape("square")
    t.shapesize(0.5)
    t.color(r, g, b)
    t.speed(0)
    t.penup()
    t.goto(random.randint(-wei, wei), random.randint(-hei, hei))
    tun.append(t)
  
#Function used to deactivate the keys
def de_activate():
  screen.onkey(None, "t")
  screen.onkey(None, "b")
  #--------------------------
  screen.onkey(None, "Up")
  screen.onkey(None, "Down")
  screen.onkey(None, "Right")
  screen.onkey(None, "Left")
  #--------------------------
  screen.onkey(None, "w")
  screen.onkey(None, "s")
  screen.onkey(None, "d")
  screen.onkey(None, "a")

#Winning functions text
def Wrote1():
  global style2p
  Writer.write(Name1+' WON!', font=style2p, align='center')
#----------------------------------------------------------
def Wrote2():
  global style2p
  Writer.write(Name2+' WON!', font=style2p, align='center')
  
#Code for checking the borders and moving the players
def control():
  global counter_1, counter_2
  #------------------------------------------
  while True:
    X = player.xcor()
    Y = player.ycor()
    dist_1 = counter_1*10-32
    #--------------------------------------------------------------------
    if X>-wei+dist_1 and X<wei-dist_1 and Y>-hei+dist_1 and Y<hei-dist_1:
      check()
      if counter_1 >= Size:
        break
      else:
        player.forward(2)
    #--------------------
    else:
      de_activate()
      Wrote2()
      break
    #-----------------
    x = player2.xcor()
    y = player2.ycor()
    dist_2 = counter_2*10-32
    #--------------------------------------------------------------------
    if x>-wei+dist_2 and x<wei-dist_2 and y>-hei+dist_2 and y<hei-dist_2:
      check2()
      if counter_2 >= Size:
        break
      else:
        player2.forward(2)
    #---------------------
    else:
      de_activate()
      Wrote1()
      break

#Code for the checking of the food and size
def check():
  global wei, hei, counter_1
  #-------------------------
  for i in range(targets):
    if player.distance(tun[i]) < 10*counter_1:
      tun[i].goto(random.randint(-wei, wei), random.randint(-hei, hei))
      #----------------------------------------------------------------
      counter_1 = round(counter_1+0.1, 1)
      player.shapesize(counter_1, counter_1)
      if counter_1 >= Size:
        de_activate()
        Wrote1()
        
      #This part of check keeps track of score for player
      if theme == "dark":
        points1.color("black")
      else:
        points1.color("white")
      #-----------------------------------------
      points1.write(chr(9608).join(
        [chr(9608) for i in range(len(Name1)+8)]
      ), font=style, align="right")
      #-------------------------------------------------------------------------------
      points1.color("red")
      points1.write(Name1+" has "+str(counter_1)+" points", font=style, align='right')

def check2():
  global wei, hei, counter_2
  #-------------------------
  for i in range(targets):
    if player2.distance(tun[i]) < 10*counter_2:
      tun[i].goto(random.randint(-wei, wei), random.randint(-hei, hei))
      #----------------------------------------------------------------
      counter_2 = round(counter_2+0.1, 1)
      player2.shapesize(counter_2, counter_2)
      if counter_2 >= Size:
        de_activate()
        Wrote2()

      #This part of check2 keeps track of score for player2
      if theme == "dark":
        points2.color("black")
      else:
        points2.color("white")
      #-----------------------------------------
      points2.write(chr(9608).join(
        [chr(9608) for i in range(len(Name2)+8)]
      ), font=style, align="left")
      #------------------------------------------------------------------------------
      points2.color("purple")
      points2.write(Name2+" has "+str(counter_2)+" points", font=style, align='left')

#Functions for the players moves
def MoveUp(): 
  player.setheading(90)
#-----------------------
def MoveDown():
  player.setheading(270)
#-----------------------
def TurnRight():
  player.setheading(0)
#-----------------------    
def TurnLeft():
  player.setheading(180)

#Functions for the players2 moves
def MoveW():
  player2.setheading(90)
#------------------------
def TurnD():
  player2.setheading(0)
#------------------------  
def TurnA():
  player2.setheading(180)
#------------------------  
def MoveS():
  player2.setheading(270)
  
#Code for making the box
boxer.penup()
boxer.goto(-wei-35, -hei-35)
boxer.pendown()
#---------------------------
for i in range(2):
  boxer.forward(wei*2+70)
  boxer.left(90)
  boxer.forward(hei*2+70)
  boxer.left(90)
boxer.width(1)

#code for making the grid
boxer.speed(0)
for i in range(int((2*(wei+40))/30)):
  boxer.color("#edcebb")
  boxer.forward(30)
  boxer.setheading(90)
  boxer.forward(2*(hei+35))
  boxer.backward(2*(hei+35))
  boxer.setheading(0)
#---------------------------
boxer.setheading(90)
for i in range(int((2*(hei+40))/30)):
  boxer.color("#edcebb")
  boxer.forward(30)
  boxer.setheading(180)
  boxer.forward(2*(wei+40)-10)
  boxer.backward(2*(wei+40)-10)
  boxer.setheading(90)

#code for making the edges crisp
for pp in range(5):
  boxer.undo()
boxer.hideturtle()

#Code for the keys and ending code
screen.onkey(PressT, "t")
screen.onkey(control, "b")
#-------------------------------
screen.onkey(MoveUp, "Up")
screen.onkey(MoveDown, "Down")
screen.onkey(TurnRight, "Right")
screen.onkey(TurnLeft, "Left")
#-------------------------------
screen.onkey(MoveW, "w")
screen.onkey(MoveS, "s")
screen.onkey(TurnD, "d")
screen.onkey(TurnA, "a")
#-------------------------------
screen.listen()
turtle.done()
