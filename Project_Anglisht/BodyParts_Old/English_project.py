
import turtle
import random
turtle.colormode(255)
turtle.bgcolor(162, 246, 252)
screen = turtle.Screen()
screen.setup(600, 800)
screen.title("Body parts")
#--------------------------------------------------------------------
ty = 0
#................................................................
win_ = 0
Gm_over_ = 0
#................................................................
e = 0
m = 0
h = 0
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def Game_over():
  turtle.clearscreen()
  turtle.colormode(255)
  turtle.bgcolor(162, 246, 252)
  #--------------------------------------------------------------------
  screen.addshape("./Images/Image_for_setup/Game_over.gif")
  screen.addshape("./Images/Image_for_setup/Try_again.gif")
  screen.addshape("./Images/Image_for_setup/Copyright.gif")
  #--------------------------------------------------------------------
  Game_over_button = turtle.Turtle()
  Game_over_button.shape("./Images/Image_for_setup/Game_over.gif")
  Game_over_button.speed(0)
  Game_over_button.penup()
  Game_over_button.goto(0, 160)
  
  Try_Again_button = turtle.Turtle()
  Try_Again_button.shape("./Images/Image_for_setup/Try_again.gif")
  Try_Again_button.speed(0)
  Try_Again_button.penup()
  Try_Again_button.goto(0, -70)

  cop_right_tag = turtle.Turtle()
  cop_right_tag.shape("./Images/Image_for_setup/Copyright.gif")
  cop_right_tag.speed(0)
  cop_right_tag.penup()
  cop_right_tag.goto(-110, -385)

  ano_choi = turtle.Turtle()
  ano_choi.speed(0)
  ano_choi.hideturtle()
  ano_choi.penup()
  #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  def gm_ov(x, y):
    ano_choi.goto(x, y)
    if ano_choi.distance(Try_Again_button) < 30:
      Opening_turtle()
  #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\    
  screen.onscreenclick(gm_ov)
  screen.listen()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def Game_win():
  turtle.clearscreen()
  turtle.colormode(255)
  turtle.bgcolor(162, 246, 252)
  #--------------------------------------------------------------------
  screen.addshape("./Images/Image_for_setup/Game_won.gif")
  screen.addshape("./Images/Image_for_setup/Click_there.gif")
  screen.addshape("./Images/Image_for_setup/Copyright.gif")
  #--------------------------------------------------------------------
  Game_won_button = turtle.Turtle()
  Game_won_button.shape("./Images/Image_for_setup/Game_won.gif")
  Game_won_button.speed(0)
  Game_won_button.penup()
  Game_won_button.goto(0,160)
  
  Go_back_button = turtle.Turtle()
  Go_back_button.shape("./Images/Image_for_setup/Click_there.gif")
  Go_back_button.speed(0)
  Go_back_button.penup()
  Go_back_button.goto(0, -155)

  cop_left_tag = turtle.Turtle()
  cop_left_tag.shape("./Images/Image_for_setup/Copyright.gif")
  cop_left_tag.speed(0)
  cop_left_tag.penup()
  cop_left_tag.goto(-110, -385)

  laa_hu = turtle.Turtle()
  laa_hu.speed(0)
  laa_hu.hideturtle()
  laa_hu.penup()
  #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  def gm_wo(x, y):
    laa_hu.goto(x, y)
    if laa_hu.distance(Go_back_button) < 70:
      global e
      global m
      global h
      if e == 1 and m == 1 and h == 1:
        scre_wn_ge()
      else:
        Opening_turtle()
  #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\    
  screen.onscreenclick(gm_wo)
  screen.listen()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def scre_wn_ge():
  turtle.clearscreen()
  turtle.colormode(255)
  turtle.bgcolor("black")
  #--------------------------------------------------------------------
  screen.addshape("./Images/Image_for_setup/End_win.gif")
  end_win_tag = turtle.Turtle()
  end_win_tag.shape("./Images/Image_for_setup/End_win.gif")
  end_win_tag.speed(0)
  end_win_tag.penup()
  end_win_tag.goto(0, 280)

  ma_fuba = turtle.Turtle()
  ma_fuba.speed(0)
  ma_fuba.hideturtle()
  ma_fuba.penup()
  #--------------------------------------------------------------------
  t = turtle.Turtle()
  t.hideturtle()
  t.speed(0)
  #--------------------------------------------------------------------
  while True:
    dist = random.randint(50, 200)
    poi = [10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90]
    ang = random.choice(poi)
    #................................................................
    x = random.randint(-100, 100)
    y = random.randint(-200, 50)
    #................................................................
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    #--------------------------------------------------------------------
    t.color(r, g, b)
    t.penup()
    t.goto(x, y)
    t.pendown()
    #--------------------------------------------------------------------
    global ty
    ty = ty + 1
    #--------------------------------------------------------------------
    if ty == 10:
      t.reset()
      t.hideturtle()
      t.speed(0)
      ty = 0
    #--------------------------------------------------------------------
    else:
      for i in range(int(360/(ang))):
        t.forward(dist)
        t.left(180-ang)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def Opening_turtle():
  turtle.clearscreen()
  turtle.colormode(255)
  turtle.bgcolor(162, 246, 252)
  #--------------------------------------------------------------------
  screen.addshape("./Images/Image_for_setup/Name.gif")
  screen.addshape("./Images/Image_for_setup/Copyright.gif")
  #--------------------------------------------------------------------
  screen.addshape("./Images/Image_for_setup/Hard.gif")
  screen.addshape("./Images/Image_for_setup/Easy.gif")
  screen.addshape("./Images/Image_for_setup/Medium.gif")
  #--------------------------------------------------------------------
  which_choice = turtle.Turtle()
  which_choice.speed(0)
  which_choice.hideturtle()
  which_choice.penup()

  game_name_tag = turtle.Turtle()
  game_name_tag.shape("./Images/Image_for_setup/Name.gif")
  game_name_tag.speed(0)
  game_name_tag.penup()
  game_name_tag.goto(0, 250)
  
  cop_right_tag = turtle.Turtle()
  cop_right_tag.shape("./Images/Image_for_setup/Copyright.gif")
  cop_right_tag.speed(0)
  cop_right_tag.penup()
  cop_right_tag.goto(-110, -385)
  #--------------------------------------------------------------------
  easy_button = turtle.Turtle()
  easy_button.shape("./Images/Image_for_setup/Easy.gif")
  easy_button.speed(0)
  easy_button.penup()
  easy_button.goto(0, 50)

  medium_button = turtle.Turtle()
  medium_button.shape("./Images/Image_for_setup/Medium.gif")
  medium_button.speed(0)
  medium_button.penup()
  medium_button.goto(0, -50)

  hard_button = turtle.Turtle()
  hard_button.shape("./Images/Image_for_setup/Hard.gif")
  hard_button.speed(0)
  hard_button.penup()
  hard_button.goto(0, -150)
  #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  def Esay_mode():
    turtle.clearscreen()
    turtle.colormode(255)
    turtle.bgcolor(247, 119, 202)
    #--------------------------------------------------------------------
    screen.addshape("./Images/Image_for_easy/Easy_menu.gif")
    screen.addshape("./Images/Image_for_easy/Easy_name.gif")
    screen.addshape("./Images/Image_for_easy/Head.gif")
    #................................................................
    screen.addshape("./Images/Image_for_easy/3_lifes.gif")
    screen.addshape("./Images/Image_for_easy/2_lifes.gif")
    screen.addshape("./Images/Image_for_easy/1_life.gif")
    screen.addshape("./Images/Image_for_easy/0_life.gif")
    #................................................................
    screen.addshape("./Images/Image_for_easy/Eyeball.gif")
    screen.addshape("./Images/Image_for_easy/Earlobe.gif")
    screen.addshape("./Images/Image_for_easy/Tooth.gif")
    #................................................................
    screen.addshape("./Images/Image_for_easy/A)_Easy.gif")
    screen.addshape("./Images/Image_for_easy/B)_Easy.gif")
    screen.addshape("./Images/Image_for_easy/C)_Easy.gif")
    #--------------------------------------------------------------------
    My_own = turtle.Turtle()
    My_own.speed(0)
    My_own.hideturtle()
    My_own.penup()
    #--------------------------------------------------------------------
    easy_menu = turtle.Turtle()
    easy_menu.shape("./Images/Image_for_easy/Easy_menu.gif")
    easy_menu.speed(0)
    easy_menu.penup()
    easy_menu.goto(-250, 300)
    
    easy_name_tag = turtle.Turtle()
    easy_name_tag.shape("./Images/Image_for_easy/Easy_name.gif")
    easy_name_tag.speed(0)
    easy_name_tag.penup()
    easy_name_tag.goto(0, 340)
    
    easy_back = turtle.Turtle()
    easy_back.shape("./Images/Image_for_easy/Head.gif")
    easy_back.speed(0)
    easy_back.penup()
    easy_back.goto(0, 70)
    
    easy_life = turtle.Turtle()
    easy_life.shape("./Images/Image_for_easy/3_lifes.gif")
    easy_life.speed(0)
    easy_life.penup()
    easy_life.goto(250, 380)
    #--------------------------------------------------------------------
    eye_spot = turtle.Turtle()
    eye_spot.shape("square")
    eye_spot.shapesize(4, 3)
    eye_spot.speed(0)
    eye_spot.penup()
    eye_spot.goto(58, 78)
  
    ear_spot = turtle.Turtle()
    ear_spot.shape("square")
    ear_spot.shapesize(6, 2)
    ear_spot.speed(0)
    ear_spot.right(22)
    ear_spot.penup()
    ear_spot.goto(135, 62)
      
    tooth_spot = turtle.Turtle()
    tooth_spot.shape("square")
    tooth_spot.shapesize(2, 3)
    tooth_spot.speed(0)
    tooth_spot.penup()
    tooth_spot.goto(-30, -40)
    #--------------------------------------------------------------------
    easy_a = turtle.Turtle()
    easy_a.shape("./Images/Image_for_easy/A)_Easy.gif")
    easy_a.speed(0)
    easy_a.penup()
    easy_a.goto(-200, -230)
    
    easy_b = turtle.Turtle()
    easy_b.shape("./Images/Image_for_easy/B)_Easy.gif")
    easy_b.speed(0)
    easy_b.penup()
    easy_b.goto(0, -230)
    
    easy_c = turtle.Turtle()
    easy_c.shape("./Images/Image_for_easy/C)_Easy.gif")
    easy_c.speed(0)
    easy_c.penup()
    easy_c.goto(200, -230)
    #--------------------------------------------------------------------
    Eye_sub = turtle.Turtle()
    Eye_sub.shape("./Images/Image_for_easy/Eyeball.gif")
    Eye_sub.speed(0)
    Eye_sub.penup()
    Eye_sub.goto(-200, -300)
    
    Ear_sub = turtle.Turtle()
    Ear_sub.shape("./Images/Image_for_easy/Earlobe.gif")
    Ear_sub.speed(0)
    Ear_sub.penup()
    Ear_sub.goto(0, -300)
    
    Teeth_sub = turtle.Turtle()
    Teeth_sub.shape("./Images/Image_for_easy/Tooth.gif")
    Teeth_sub.speed(0)
    Teeth_sub.penup()
    Teeth_sub.goto(200, -300)  
    #--------------------------------------------------------------------
    t_easy = turtle.Turtle()
    t_easy.speed(0)
    t_easy.hideturtle()
    t_easy.color("lime")
    t_easy.width(6)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def easy_ga_ov():
      global Gm_over_
      Gm_over_ += 1
      #................................................................ 
      if Gm_over_ == 1:
        easy_life.shape("./Images/Image_for_easy/2_lifes.gif")
      elif Gm_over_ == 2:
        easy_life.shape("./Images/Image_for_easy/1_life.gif")
      elif Gm_over_ == 3:
        easy_life.shape("./Images/Image_for_easy/0_life.gif")
      else:
        Gm_over_ = 0
        Game_over()
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def easy_ga_wi():
      global Gm_over_
      global win_
      global e
      win_ += 1
      #................................................................ 
      if win_ == 3:
        Gm_over_ = 0
        win_ = 0
        e = 1
        Game_win()
      elif win_ < 3:
        screen.onscreenclick(Easy_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Easy_A_choice(x, y):
      My_own.goto(x, y)
      #--------------------------------------------------------------------
      if My_own.distance(eye_spot) < 30:
        eye_spot.reset()
        eye_spot.hideturtle()
        #................................................................
        t_easy.penup()
        t_easy.goto(29, 50)
        t_easy.pendown()
        #................................................................
        for i in range(2):
          t_easy.forward(60)
          t_easy.left(90)
          t_easy.forward(80)
          t_easy.left(90)
        #................................................................ 
        easy_ga_wi()
      #--------------------------------------------------------------------
      elif My_own.distance(ear_spot) < 20 or My_own.distance(tooth_spot) < 20:
        easy_ga_ov()
      #--------------------------------------------------------------------
      else:
        screen.onscreenclick(Easy_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Easy_B_choice(x, y):
      My_own.goto(x, y)
      #--------------------------------------------------------------------
      if My_own.distance(ear_spot) < 20:
        ear_spot.reset()
        ear_spot.hideturtle()
        #................................................................
        t_easy.penup()
        t_easy.goto(100, 2)
        t_easy.pendown()
        #................................................................
        for i in range(2):
          t_easy.forward(65)
          t_easy.left(90)
          t_easy.forward(110)
          t_easy.left(90)
        #................................................................ 
        easy_ga_wi()
      #--------------------------------------------------------------------
      elif My_own.distance(eye_spot) < 30 or My_own.distance(tooth_spot) < 20:
        easy_ga_ov()
      #--------------------------------------------------------------------
      else:
        screen.onscreenclick(Easy_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Easy_C_choice(x, y):
      My_own.goto(x, y)
      #--------------------------------------------------------------------
      if My_own.distance(tooth_spot) < 20:
        tooth_spot.reset()
        tooth_spot.hideturtle()
        #................................................................
        t_easy.penup()
        t_easy.goto(-60, -60)
        t_easy.pendown()
        #................................................................
        for i in range(2):
          t_easy.forward(60)
          t_easy.left(90)
          t_easy.forward(50)
          t_easy.left(90)
        #................................................................ 
        easy_ga_wi()
      #--------------------------------------------------------------------
      elif My_own.distance(eye_spot) < 30 or My_own.distance(ear_spot) < 20:
        easy_ga_ov()
      #--------------------------------------------------------------------
      else:
        screen.onscreenclick(Easy_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Easy_choice(x, y):
      My_own.goto(x, y)
      if My_own.distance(Eye_sub) < 50:
        screen.onscreenclick(Easy_A_choice)
      elif My_own.distance(Ear_sub) < 50:
        screen.onscreenclick(Easy_B_choice)
      elif My_own.distance(Teeth_sub) < 50:
        screen.onscreenclick(Easy_C_choice)
      elif My_own.distance(easy_menu) < 20:
        global Gm_over_
        global win_
        Gm_over_ = 0
        win_ = 0
        Opening_turtle()
      else:
        screen.onscreenclick(Easy_choice)
    #--------------------------------------------------------------------
    screen.onscreenclick(Easy_choice)         
  #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  def Medium_mode():
    turtle.clearscreen()
    turtle.colormode(255)
    turtle.bgcolor(200, 191, 231)
    #--------------------------------------------------------------------
    screen.addshape("./Images/Image_for_medium/Medium_menu.gif")
    screen.addshape("./Images/Image_for_medium/Medium_name.gif")
    screen.addshape("./Images/Image_for_medium/Abnomen.gif")
    #...................................................................
    screen.addshape("./Images/Image_for_medium/3_lifes.gif")
    screen.addshape("./Images/Image_for_medium/2_lifes.gif")
    screen.addshape("./Images/Image_for_medium/1_life.gif")
    screen.addshape("./Images/Image_for_medium/0_life.gif")
    #...................................................................
    screen.addshape("./Images/Image_for_medium/A)_Medium.gif")
    screen.addshape("./Images/Image_for_medium/B)_Medium.gif")
    screen.addshape("./Images/Image_for_medium/C)_Medium.gif")
    #...................................................................
    screen.addshape("./Images/Image_for_medium/Bladder.gif")
    screen.addshape("./Images/Image_for_medium/Kidney.gif")
    screen.addshape("./Images/Image_for_medium/Lung.gif")
    #--------------------------------------------------------------------
    Mio_umo = turtle.Turtle()
    Mio_umo.speed(0)
    Mio_umo.hideturtle()
    Mio_umo.penup()
    #--------------------------------------------------------------------
    medium_menu = turtle.Turtle()
    medium_menu.shape("./Images/Image_for_medium/Medium_menu.gif")
    medium_menu.speed(0)
    medium_menu.penup()
    medium_menu.goto(-230, 370)
    
    medium_name_tag = turtle.Turtle()
    medium_name_tag.shape("./Images/Image_for_medium/Medium_name.gif")
    medium_name_tag.speed(0)
    medium_name_tag.penup()
    medium_name_tag.goto(0, 300)
        
    medium_back = turtle.Turtle()
    medium_back.shape("./Images/Image_for_medium/Abnomen.gif")
    medium_back.speed(0)
    medium_back.penup()
    medium_back.goto(0, 10)
    
    medium_life = turtle.Turtle()
    medium_life.shape("./Images/Image_for_medium/3_lifes.gif")
    medium_life.speed(0)
    medium_life.penup()
    medium_life.goto(250, 380)
    #--------------------------------------------------------------------
    bladder_spot = turtle.Turtle()
    bladder_spot.shape("square")
    bladder_spot.shapesize(3.5, 5)
    bladder_spot.speed(0)
    bladder_spot.penup()
    bladder_spot.goto(0, -190)
  
    kidney_spot = turtle.Turtle()
    kidney_spot.shape("square")
    kidney_spot.shapesize(3, 3)
    kidney_spot.speed(0)
    kidney_spot.penup()
    kidney_spot.goto(70, -10)
  
    lung_spot = turtle.Turtle()
    lung_spot.shape("square")
    lung_spot.shapesize(8, 6)
    lung_spot.speed(0)
    lung_spot.penup()
    lung_spot.goto(70, 150)
    #--------------------------------------------------------------------
    medium_a = turtle.Turtle()
    medium_a.shape("./Images/Image_for_medium/A)_Medium.gif")
    medium_a.speed(0)
    medium_a.penup()
    medium_a.goto(-200, -230)
  
    medium_b = turtle.Turtle()
    medium_b.shape("./Images/Image_for_medium/B)_Medium.gif")
    medium_b.speed(0)
    medium_b.penup()
    medium_b.goto(0, -250)
  
    medium_c = turtle.Turtle()
    medium_c.shape("./Images/Image_for_medium/C)_Medium.gif")
    medium_c.speed(0)
    medium_c.penup()
    medium_c.goto(190, -230)
    #--------------------------------------------------------------------
    Bladder_sub = turtle.Turtle()
    Bladder_sub.shape("./Images/Image_for_medium/Bladder.gif")
    Bladder_sub.speed(0)
    Bladder_sub.penup()
    Bladder_sub.goto(-200, -320)
  
    Kidney_sub = turtle.Turtle()
    Kidney_sub.shape("./Images/Image_for_medium/Kidney.gif")
    Kidney_sub.speed(0)
    Kidney_sub.penup()
    Kidney_sub.goto(0, -330)
  
    Lung_sub = turtle.Turtle()
    Lung_sub.shape("./Images/Image_for_medium/Lung.gif")
    Lung_sub.speed(0)
    Lung_sub.penup()
    Lung_sub.goto(190, -320)
    #--------------------------------------------------------------------
    t_medium = turtle.Turtle()
    t_medium.speed(0)
    t_medium.hideturtle()
    t_medium.color("lime")
    t_medium.width(6)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def medium_ga_ov():
      global Gm_over_
      Gm_over_ += 1
      #................................................................ 
      if Gm_over_ == 1:
        medium_life.shape("./Images/Image_for_medium/2_lifes.gif")
      elif Gm_over_ == 2:
        medium_life.shape("./Images/Image_for_medium/1_life.gif")
      elif Gm_over_ == 3:
        medium_life.shape("./Images/Image_for_medium/0_life.gif")
      else:
        Gm_over_ = 0
        Game_over()
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def medium_ga_wi():
      global Gm_over_
      global win_
      global m
      win_ += 1
      #................................................................ 
      if win_ == 3:
        Gm_over_ = 0
        win_ = 0
        m = 1
        Game_win()
      elif win_ < 3:
        screen.onscreenclick(Medium_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Medium_A_choice(x, y):
      Mio_umo.goto(x, y)
      #--------------------------------------------------------------------
      if Mio_umo.distance(bladder_spot) < 30:
        bladder_spot.reset()
        bladder_spot.hideturtle()
        #................................................................
        t_medium.penup()
        t_medium.goto(-50, -220)
        t_medium.pendown()
        #................................................................
        for i in range(2):
          t_medium.forward(100)
          t_medium.left(90)
          t_medium.forward(60)
          t_medium.left(90)
        #................................................................ 
        medium_ga_wi()   
      #--------------------------------------------------------------------
      elif Mio_umo.distance(kidney_spot) < 20 or Mio_umo.distance(lung_spot) < 50:
        medium_ga_ov()
      #--------------------------------------------------------------------
      else:
        screen.onscreenclick(Medium_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Medium_B_choice(x, y):
      Mio_umo.goto(x, y)
      #--------------------------------------------------------------------
      if Mio_umo.distance(kidney_spot) < 20:
        kidney_spot.reset()
        kidney_spot.hideturtle()
        #................................................................
        t_medium.penup()
        t_medium.goto(40, -40)
        t_medium.pendown()
        #................................................................
        for i in range(2):
          t_medium.forward(50)
          t_medium.left(90)
          t_medium.forward(60)
          t_medium.left(90)
        #................................................................ 
        medium_ga_wi()
      #--------------------------------------------------------------------
      elif Mio_umo.distance(bladder_spot) < 30 or Mio_umo.distance(lung_spot) < 50:
        medium_ga_ov()
      #--------------------------------------------------------------------
      else:
        screen.onscreenclick(Medium_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Medium_C_choice(x, y):
      Mio_umo.goto(x, y)
      #--------------------------------------------------------------------
      if Mio_umo.distance(lung_spot) < 50:
        lung_spot.reset()
        lung_spot.hideturtle()
        #................................................................
        t_medium.penup()
        t_medium.goto(5, 75)
        t_medium.pendown()
        #................................................................
        for i in range(2):
          t_medium.forward(125)
          t_medium.left(90)
          t_medium.forward(155)
          t_medium.left(90)
        #................................................................ 
        medium_ga_wi()
      #--------------------------------------------------------------------
      elif Mio_umo.distance(bladder_spot) < 30 or Mio_umo.distance(kidney_spot) < 20:
        medium_ga_ov()
      #--------------------------------------------------------------------
      else:
        screen.onscreenclick(Medium_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Medium_choice(x, y):
      Mio_umo.goto(x, y)
      if Mio_umo.distance(Bladder_sub) < 50:
        screen.onscreenclick(Medium_A_choice)
      elif Mio_umo.distance(Kidney_sub) < 50:
        screen.onscreenclick(Medium_B_choice)
      elif Mio_umo.distance(Lung_sub) < 50:
        screen.onscreenclick(Medium_C_choice)
      elif Mio_umo.distance(medium_menu) < 20:
        global Gm_over_
        global win_
        Gm_over_ = 0
        win_ = 0
        Opening_turtle()
      else:
        screen.onscreenclick(Medium_choice)
    #--------------------------------------------------------------------
    screen.onscreenclick(Medium_choice)          
  #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  
  def Hard_mode():
    turtle.clearscreen()
    turtle.colormode(255)
    turtle.bgcolor(0, 0, 255)
    #--------------------------------------------------------------------
    screen.addshape("./Images/Image_for_hard/Hard_menu.gif")
    screen.addshape("./Images/Image_for_hard/Hard_name.gif")
    screen.addshape("./Images/Image_for_hard/Leg_bones.gif")
    #................................................................
    screen.addshape("./Images/Image_for_hard/3_lifes.gif")
    screen.addshape("./Images/Image_for_hard/2_lifes.gif")
    screen.addshape("./Images/Image_for_hard/1_life.gif")
    screen.addshape("./Images/Image_for_hard/0_life.gif")
    #................................................................
    screen.addshape("./Images/Image_for_hard/A)_Hard.gif")
    screen.addshape("./Images/Image_for_hard/B)_Hard.gif")
    screen.addshape("./Images/Image_for_hard/C)_Hard.gif")
    #................................................................
    screen.addshape("./Images/Image_for_hard/Fibula.gif")
    screen.addshape("./Images/Image_for_hard/Calcaneus.gif")
    screen.addshape("./Images/Image_for_hard/Femur.gif")
    #--------------------------------------------------------------------
    Mo_cose = turtle.Turtle()
    Mo_cose.speed(0)
    Mo_cose.hideturtle()
    Mo_cose.penup()
    #--------------------------------------------------------------------
    hard_menu = turtle.Turtle()
    hard_menu.shape("./Images/Image_for_hard/Hard_menu.gif")
    hard_menu.speed(0)
    hard_menu.penup()
    hard_menu.goto(-220, 375)
  
    hard_name_tag = turtle.Turtle()
    hard_name_tag.shape("./Images/Image_for_hard/Hard_name.gif")
    hard_name_tag.speed(0)
    hard_name_tag.penup()
    hard_name_tag.goto(-5, 300)
  
    hard_back = turtle.Turtle()
    hard_back.shape("./Images/Image_for_hard/Leg_bones.gif")
    hard_back.speed(0)
    hard_back.penup()
    hard_back.goto(-150, -60)
  
    hard_life = turtle.Turtle()
    hard_life.shape("./Images/Image_for_hard/3_lifes.gif")
    hard_life.speed(0)
    hard_life.penup()
    hard_life.goto(250, 380)
    #--------------------------------------------------------------------
    fibula_spot = turtle.Turtle()
    fibula_spot.shape("square")
    fibula_spot.shapesize(12.3, 1.4)
    fibula_spot.speed(0)
    fibula_spot.penup()
    fibula_spot.goto(-220, -163)
  
    calcaneus_spot = turtle.Turtle()
    calcaneus_spot.shape("square")
    calcaneus_spot.shapesize(1.5, 1.5)
    calcaneus_spot.speed(0)
    calcaneus_spot.penup()
    calcaneus_spot.goto(-160, -285)
  
    femur_spot = turtle.Turtle()
    femur_spot.shape("square")
    femur_spot.shapesize(12.5, 3)
    femur_spot.speed(0)
    femur_spot.penup()
    femur_spot.goto(-145, 80)
    #--------------------------------------------------------------------
    hard_a = turtle.Turtle()
    hard_a.shape("./Images/Image_for_hard/A)_Hard.gif")
    hard_a.speed(0)
    hard_a.penup()
    hard_a.goto(90, 210)
  
    hard_b = turtle.Turtle()
    hard_b.shape("./Images/Image_for_hard/B)_Hard.gif")
    hard_b.speed(0)
    hard_b.penup()
    hard_b.goto(90, 0)
  
    hard_c = turtle.Turtle()
    hard_c.shape("./Images/Image_for_hard/C)_Hard.gif")
    hard_c.speed(0)
    hard_c.penup()
    hard_c.goto(90, -190)
    #--------------------------------------------------------------------
    Fibula_sub = turtle.Turtle()
    Fibula_sub.shape("./Images/Image_for_hard/Fibula.gif")
    Fibula_sub.speed(0)
    Fibula_sub.penup()
    Fibula_sub.goto(90, 130)
  
    Calcaneus_sub = turtle.Turtle()
    Calcaneus_sub.shape("./Images/Image_for_hard/Calcaneus.gif")
    Calcaneus_sub.speed(0)
    Calcaneus_sub.penup()
    Calcaneus_sub.goto(90, -80)
  
    Femur_sub = turtle.Turtle()
    Femur_sub.shape("./Images/Image_for_hard/Femur.gif")
    Femur_sub.speed(0)
    Femur_sub.penup()
    Femur_sub.goto(90, -280)
    #--------------------------------------------------------------------
    t_hard = turtle.Turtle()
    t_hard.speed(0)
    t_hard.hideturtle()
    t_hard.color("lime")
    t_hard.width(6)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def hard_ga_ov():
      global Gm_over_
      Gm_over_ += 1
      #................................................................ 
      if Gm_over_ == 1:
        hard_life.shape("./Images/Image_for_hard/2_lifes.gif")
      elif Gm_over_ == 2:
        hard_life.shape("./Images/Image_for_hard/1_life.gif")
      elif Gm_over_ == 3:
        hard_life.shape("./Images/Image_for_hard/0_life.gif")
      else:
        Gm_over_ = 0
        Game_over()
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def hard_ga_wi():
      global Gm_over_
      global win_
      global h
      win_ += 1
      #................................................................ 
      if win_ == 3:
        Gm_over_ = 0
        win_ = 0
        h = 1
        Game_win()
      elif win_ < 3:
        screen.onscreenclick(Hard_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Hard_A_choice(x, y):
      Mo_cose.goto(x, y)
      #--------------------------------------------------------------------
      if Mo_cose.distance(fibula_spot) < 40:
        fibula_spot.reset()
        fibula_spot.hideturtle()
        #................................................................
        t_hard.penup()
        t_hard.goto(-240, -290)
        t_hard.pendown()
        #................................................................
        for i in range(2):
          t_hard.forward(30)
          t_hard.left(90)
          t_hard.forward(240)
          t_hard.left(90)
        #................................................................
        hard_ga_wi()  
      #--------------------------------------------------------------------
      elif Mo_cose.distance(calcaneus_spot) < 20 or Mo_cose.distance(femur_spot) < 50:
        hard_ga_ov()
      #--------------------------------------------------------------------
      else:
        screen.onscreenclick(Hard_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Hard_B_choice(x, y):
      Mo_cose.goto(x, y)
      #--------------------------------------------------------------------
      if Mo_cose.distance(calcaneus_spot) < 20:
        calcaneus_spot.reset()
        calcaneus_spot.hideturtle()
        #................................................................
        t_hard.penup()
        t_hard.goto(-170, -300)
        t_hard.pendown()
        #................................................................
        for i in range(2):
          t_hard.forward(30)
          t_hard.left(90)
          t_hard.forward(25)
          t_hard.left(90)
        #................................................................ 
        hard_ga_wi()
      #--------------------------------------------------------------------
      elif Mo_cose.distance(fibula_spot) < 40 or Mo_cose.distance(femur_spot) < 50:
        hard_ga_ov()
      #--------------------------------------------------------------------
      else:
        screen.onscreenclick(Hard_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Hard_C_choice(x, y):
      Mo_cose.goto(x, y)
      #--------------------------------------------------------------------
      if Mo_cose.distance(femur_spot) < 50:
        femur_spot.reset()
        femur_spot.hideturtle()
        #................................................................
        t_hard.penup()
        t_hard.goto(-170, -50)
        t_hard.pendown()
        #................................................................
        for i in range(2):
          t_hard.forward(60)
          t_hard.left(90)
          t_hard.forward(250)
          t_hard.left(90)
        #................................................................
        hard_ga_wi()
      #--------------------------------------------------------------------
      elif Mo_cose.distance(fibula_spot) < 40 or Mo_cose.distance(calcaneus_spot) < 20:
        hard_ga_ov()
      #--------------------------------------------------------------------
      else:
        screen.onscreenclick(Hard_choice)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def Hard_choice(x, y):
      Mo_cose.goto(x, y)
      if Mo_cose.distance(Fibula_sub) < 50:
        screen.onscreenclick(Hard_A_choice)
      elif Mo_cose.distance(Calcaneus_sub) < 50:
        screen.onscreenclick(Hard_B_choice) 
      elif Mo_cose.distance(Femur_sub) < 50:
        screen.onscreenclick(Hard_C_choice)
      elif Mo_cose.distance(hard_menu) < 20:
        global Gm_over_
        global win_
        Gm_over_ = 0
        win_ = 0
        Opening_turtle()
      else:
        screen.onscreenclick(Hard_choice)
    #--------------------------------------------------------------------
    screen.onscreenclick(Hard_choice)          
  #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  def Mode_choice(x, y):
    which_choice.goto(x, y)
    if which_choice.distance(easy_button) < 30:
      Esay_mode()
    elif which_choice.distance(medium_button) < 30:
      Medium_mode()
    elif which_choice.distance(hard_button) < 30:
      Hard_mode()
    else:
      screen.onscreenclick(Mode_choice)
  #--------------------------------------------------------------------
  screen.onscreenclick(Mode_choice)
  screen.listen()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Opening_turtle()
