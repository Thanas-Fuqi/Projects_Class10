
import turtle
import time

turtle.colormode(255)
turtle.bgcolor(162, 246, 252)

screen = turtle.Screen()
screen.setup(610, 810)
screen.title("Body parts")

go_on, go_on1, go_on2, go_on3 = 1, 1, 1, 1

def Game_won():
  turtle.clearscreen()
  screen.onclick(None)
  screen.onkeypress(oppi, "x") 
  global go_on, go_on1, go_on2, go_on3, go_on4
  go_on, go_on1, go_on2, go_on3 = 1, 1, 1, 1 
  while go_on4 == 1:
    for i in range(7):
      if go_on4 == 1:
        turtle.bgpic("./Animation/Gradient_anim/Gradient_"+str(i)+".png")
        time.sleep(0.125)
        screen.update()
  
def Game_ovt():
  turtle.clearscreen()
  turtle.bgpic("./Begin_convert/Gam_oer.png")

  g = turtle.Turtle()
  g.speed(0)
  g.penup()
  g.hideturtle()
  
  def pof(x, y):
    g.goto(x, y)
    if g.distance((0, -320)) < 60:
      global go_on, go_on1, go_on2, go_on3
      go_on, go_on1, go_on2, go_on3 = 1, 1, 1, 1 
      oppi()
    else:
      screen.onclick(pof)
  
  screen.onclick(pof)

def last_stich_o():
  def cir(x, y):
    dot.goto(x, y)
    dot.pendown()
    dot.circle(3)
  
  turtle.bgpic("./Stich/Stich_b.png")
  screen.onkeypress(None, "z") 

  m = turtle.Turtle()
  m.hideturtle()
  m.speed(0)
  m.penup()

  dot = turtle.Turtle()
  dot.color("black")
  dot.hideturtle()
  dot.width(5)
  dot.speed(0)
  dot.penup()
  cir(-103, -40)

  def hun10(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(-94, -94)
      global go_on4
      go_on4 = 1
      Game_won()
    else:
      Game_ovt()

  def hun9(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(-76, -38)
      screen.onclick(hun10)
    else:
      Game_ovt()

  def hun8(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(-50, -99)
      screen.onclick(hun9)
    else:
      Game_ovt()

  def hun7(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(-26, -38)
      screen.onclick(hun8)
    else:
      Game_ovt()

  def hun6(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(2, -98)
      screen.onclick(hun7)
    else:
      Game_ovt()

  def hun5(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(31, -43)
      screen.onclick(hun6)
    else:
      Game_ovt()

  def hun4(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(22, -99)
      screen.onclick(hun5)
    else:
      Game_ovt()

  def hun3(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(-3, -39)
      screen.onclick(hun4)
    else:
      Game_ovt()

  def hun2(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(-29, -97)
      screen.onclick(hun3)
    else:
      Game_ovt()

  def hun1(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(-51, -38)
      screen.onclick(hun2)
    else:
      Game_ovt()

  def hun(x, y):
    m.goto(x, y)
    if m.distance(dot) < 20:
      cir(-75, -100)
      screen.onclick(hun1)
    else:
      Game_ovt()

  screen.onclick(hun)
  
def last_stich():
  turtle.clearscreen()
  screen.onkey(None, "Up")
  screen.onkey(None, "Down")
  screen.onkey(None, "Right")
  screen.onkey(None, "Left")
  turtle.bgpic("./Stich/Stich_a.png")
  screen.onkeypress(last_stich_o, "z") 

def First_incion3():
  step = 25
  place = (60, -86)
  screen.onclick(None)
  turtle.clearscreen()
  turtle.bgpic("./Step_by_step/First_step_e.png")
  screen.addshape("./Begin_convert/New_valve.gif")

  m = turtle.Turtle()
  m.shape("./Begin_convert/New_valve.gif")
  m.speed(0)
  m.penup()
  m.goto(-212, 68)

  def checkBorders():
    X = m.xcor()
    Y = m.ycor()
    if X>-300 and X<300 and Y>-400 and Y<400:
      return True
    else: 
      return False

  def Mov_up():
    m.setheading(90)
    m.forward(step)
    if checkBorders() == True:
      if m.distance(place) < 50:
        last_stich()
    else:
      Game_ovt()
    
  def Mov_do():
    m.setheading(270)
    m.forward(step)
    if checkBorders() == True:
      if m.distance(place) < 50:
        last_stich()
    else:
      Game_ovt()
    
  def Mov_ri():
    m.setheading(0)
    m.forward(step)
    if checkBorders() == True:
      if m.distance(place) < 50:
        last_stich()
    else:
      Game_ovt()
    
  def Mov_le():
    m.setheading(180)
    m.forward(step)
    if checkBorders() == True:
      if m.distance(place) < 50:
        last_stich()
    else:
      Game_ovt()

  screen.onkey(Mov_up, "Up")
  screen.onkey(Mov_do, "Down")
  screen.onkey(Mov_ri, "Right")
  screen.onkey(Mov_le, "Left")

def First_incion2():
  screen.onkeypress(None, "z") 
  turtle.bgpic("./Step_by_step/First_step_d.png")
  
  m = turtle.Turtle()
  m.color("red")
  m.hideturtle()
  m.width(12)
  m.speed(0)
  m.penup()

  def hop1(x, y):
    m.goto(x, y)
    if m.distance((0, -42)) < 20:
      First_incion3()
    else:
      Game_ovt()

  def hop(x, y):
    m.goto(x, y)
    if m.distance((-18, -56)) < 20:
      screen.onclick(hop1)
    else:
      Game_ovt()
      
  screen.onclick(hop)

def First_incion1():
  screen.onclick(None)
  turtle.clearscreen()
  turtle.bgpic("./Step_by_step/First_step_c.png")
  screen.onkeypress(First_incion2, "z") 
  
def First_incion():
  screen.onkeypress(None, "z") 
  turtle.bgpic("./Step_by_step/First_step_b.png")
  
  m = turtle.Turtle()
  m.color("red")
  m.hideturtle()
  m.width(12)
  m.speed(0)
  m.penup()

  def hop1(x, y):
    m.goto(x, y)
    if m.distance((33, -94)) < 30:
      First_incion1()
    else:
      Game_ovt()

  def hop(x, y):
    m.goto(x, y)
    if m.distance((-96,-94)) < 30:
      screen.onclick(hop1)
    else:
      Game_ovt()
      
  screen.onclick(hop)

def First_stepping():
  turtle.bgpic("./Step_by_step/First_step_a.png")
  screen.onkeypress(First_incion, "z") 

def oppi():
  def Convert6():
    global go_on3
    go_on3 = 0
    turtle.bgpic("./Begin_convert/Next_day_in.png")
    screen.onkeypress(First_stepping, "z") 
  
  def Convert5():
    global go_on3
    screen.onkeypress(Convert6, "z") 
    while go_on3 == 1:
      for i in range(14):
        if go_on3 == 1:
          turtle.bgpic("./Animation/Next_day_anim/The_next_day-"+str(i)+".png")
          time.sleep(0.1)
          screen.update()
  
  def Convert4():
    global go_on2
    go_on2 = 0
    turtle.bgpic("./Begin_convert/First_Converstation(2).png")
    screen.onkeypress(Convert5, "z") 
  
  def Convert3():
    global go_on2
    screen.onkeypress(Convert4, "z") 
    while go_on2 == 1:
      for i in range(13):
        if go_on2 == 1:
          turtle.bgpic("./Animation/Sec_Conserv_anim/First_Converstation(1)_"+str(i)+".png")
          time.sleep(0.1)
          screen.update()
  
  def Convert2():
    turtle.bgpic("./Begin_convert/First_Converstation.png")
    screen.onkeypress(Convert3, "z") 
  
  def Convert1():
    global go_on1
    go_on1 = 0
    turtle.bgpic("./Begin_convert/Begin_sats(1).png")
    screen.onkeypress(Convert2, "z") 
  
  def starti():
    global go_on1
    screen.onclick(None)
    screen.onkeypress(Convert1, "z")
    while go_on1 == 1:
      for i in range(14):
        if go_on1 == 1:
          turtle.bgpic("./Animation/First_conserv_anim/Begin_sats_"+str(i)+".png")
          time.sleep(0.1)
          screen.update()            

  Fir = turtle.Turtle()
  Fir.speed(0)
  Fir.penup()
  Fir.hideturtle()

  global go_on4
  go_on4 = 0
  
  def choi(x, y):
    Fir.goto(x, y)
    if Fir.distance((-10, -210)) < 100:
      global go_on 
      go_on = 0
      starti()
    else:
      screen.onclick(choi)

  screen.onclick(choi)
  
  while go_on == 1:
    for i in range(6):
      if go_on == 1:
        turtle.bgpic("./Animation/Begin_start_anim/Begin_Start("+str(i)+").png")
        time.sleep(0.125)
        screen.update()

screen.listen()
oppi()
turtle.done()
