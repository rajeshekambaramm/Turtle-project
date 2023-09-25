from turtle import*
from time import*
title("Naruto")
bgcolor("gray")
speed (999)
screensize(768,1200)
bgpic("mount.gif")
def font():
    penup()
    setposition(-270,410)
    pendown()
    sleep(.30)
    color ("#ff4000")
    write ("N",font=("Comic Sans MS",60,"italic")) 
    penup () 
    setposition(-160,410)
    pendown()
    sleep(.30)
    write ("A",font=("Comic Sans MS",55)) 
    penup () 
    setposition(-60,410)
    pendown()
    sleep(.30)
    #color ("gray")
    write ("R",font=("Comic Sans MS",55)) 
    penup () 
    setposition(40,410)
    pendown()
    sleep(.30)
    #color ("gray")
    write ("U",font=("Comic Sans MS",55))   
    penup () 
    setposition(130,410)
    pendown()
    sleep(.30)
    #color ("gray")
    write ("T",font=("Comic Sans MS",55)) 
    penup () 
    setposition(230,410)
    pendown()
    sleep(.30)
    #color ("gray")
    write ("O",font=("Comic Sans MS",55)) 
    penup () 
    setposition(-200,360)
    pendown()
    sleep(.30)
    color ("#135d63")
    write ("U",font=("Palatino",50,"bold")) 
    penup () 
    setposition(-130,360)
    pendown()
    sleep(.30)
    write ("z",font=("Palatino",40)) 
    penup () 
    setposition(-80,360)
    pendown()
    sleep(.30)
    #color ("indigo")
    write ("u",font=("Palatino",40)) 
    penup () 
    setposition(-20,360)
    pendown()
    sleep(.30)
    #color ("indigo")
    write ("m",font=("Palatino",40)) 
    penup () 
    setposition(60,360)
    pendown()
    sleep(.30)
    #color ("indigo")
    write ("a",font=("Palatino",40)) 
    penup () 
    setposition(130,360)
    pendown()
    sleep(.30)
    #color ("indigo")
    write ("k",font=("Palatino",40)) 
    penup () 
    setposition(200,360)
    pendown()
    sleep(.30)
    #color ("indigo")
    write ("i",font=("Palatino",40)) 
    penup () 
def hair():
    penup()
    right(90)
    setposition(-0,330)
    pendown()
    color ("black","yellow")
    begin_fill()
    left(90)
    forward(115)         
    right(10)                             
    circle(-40,30)       #*******-------------1-------------*******
    left(130)
    circle(40,30)   
    right(100)                          
    circle(40,30)        #*******-------------2-------------*******
    left(90)
    circle(40,30) 
    right(120)                           
    circle(40,30)        #*******-------------3-------------*******
    left(90)
    circle(40,30) 
    left(90)                         
    circle(40,-30)        #*******-------------4-------------*******
    right(60)
    circle(40,30)
    right(145)
    circle(50,30)         #*******-------------5-------------*******
    left(90)
    circle(60,30) 
    right(130)
    circle(60,30)         #*******-------------6-------------*******
    left(100)
    circle(50,30)   
    right(140)
    circle(50,30)         #*******-------------7-------------*******
    left(100)
    circle(40,30) 
    left(80)
    circle(40,-30)        #*******-------------8-------------*******
    right(60)
    circle(40,30) 
    right(130)
    circle(40,30)         #*******-------------9-------------*******
    left(90)
    circle(40,30) 
    right(140)
    circle(40,30)         #*******-------------10-------------*******
    left(100)
    circle(40,30) 
    right(120)
    circle(40,30)         #*******-------------11-------------*******
    left(135)
    circle(-60,25)
    setposition(-0,330)
    end_fill()    
    penup()                #*******------------- side hair -------------*******
    setposition(4,330)
    begin_fill()
    pendown()
    left(230)
    circle(30,90)
    left(35)
    forward(106)
    left(35)
    circle(30,90)
    setposition(4,330)
    end_fill()
def head_band():
    penup()
    setposition(7,347)
    pendown()   
    color ("black","navyblue")
    begin_fill()
    left(55)
    circle (5.5,180)
    right(180)
    circle (5.5,180)
    right(180)
    circle (5.5,180)
    right(180)
    bk(115)
    left(180)
    circle (5.5,180)
    right(180)
    circle (5.5,180)
    right(180)
    circle (5.5,180)
    setposition(7,347)
    end_fill()
    penup()                   #******---------------- band1 -----------------******
    setposition(12,343)
    pendown()
    begin_fill()
    color ("black","lightgrey")
    right(180)
    forward(103)
    circle (-5,90)
    forward(15)
    circle (-5,90)
    forward(98)
    circle (-5,90)
    setpos (9,343)
    end_fill()
    penup()                  #******---------------- leaf village symbol -----------------******
    setposition(83,339)
    pensize (2)
    pendown()
    color ("black")
    left(110)
    forward(12)
    right(70)
    circle (11,150)
    left(20)
    circle (9,150)
    left(20)
    circle (6,150)
    left(20)
    circle (3,150)
    penup()
    setpos (54,336)
    pendown()
    left(140)
    forward(12)
    left(120)
    forward(12)
def face():
    penup()
    setposition(5,313)
    pendown()
    pensize(1.5)
    color ("black","#f4b9a2")
    begin_fill()
    right(60)
    fd (20)
    right(150)               #*****---------- ear left  ----------*****
    forward(15)
    circle (6,120)
    circle (26,50)
    right(25)
    circle (26,50)
    circle (6,120)
    forward(14)
    left(15)
    bk(30)                  #*****---------- face  ----------*****
    left(180)
    circle (50,60)
    right(17)
    circle (44,90)
    right(17)
    circle (50,60)
    left(180)
    bk(40)
    left(15)                #*****---------- ear right  ----------*****
    forward(14)
    circle (6,120)
    circle (26,50)
    right(18)
    circle (26,50)
    circle (6,120)
    forward(15)
    right(150)
    forward(18)
    setposition(5,313)
    end_fill()
def eyebrow():
    penup()
    setposition(50,302)
    pendown()
    color ("black","yellow")
    begin_fill()
    right(-55)
    circle (4,-180)
    bk(23)
    right(155)
    circle (90,10)
    left(10)
    circle (190,-7)
    right(39)
    bk(23)
    end_fill()
    penup()                   #*****---------- eye brow right   ----------*****
    setposition(77,302)
    pendown()
    begin_fill()
    left(65)
    circle (4,180)
    forward(23)
    left(155)
    circle (90,-10)
    right(5)
    circle (-190,7)
    left(49)
    forward(23)
    end_fill() 
def bandhair():
    penup()                #*****--------- right hair ----------*****
    pensize(1)
    setposition(40,350)
    color('black',"yellow")
    begin_fill()
    left(45)
    pendown()
    forward(30)
    right(150)
    forward(25)
    left(150)
    forward(25)
    right(150)
    forward(30)
    end_fill()
    penup()                  #*****--------- left hair ----------*****
    setposition(120,350)
    begin_fill()
    left(140)
    pendown()
    forward(30)
    right(150)
    forward(25)
    left(150)
    forward(25)
    right(150)
    forward(25)
    end_fill()   
def eye():
    penup()                #*****--------- right eye ----------*****
    setposition(47,287)
    pendown()
    color ("black","white")
    begin_fill()
    left(229)
    bk(7)
    right(10)
    circle (-20,-50)
    left(10)
    bk(7)                                       ########
    right(110)
    forward(20)                                      ########
    left(60)
    circle (20,90)
    setposition(47,287)
    end_fill()
    penup()                      #*****--------- right eye ----------*****
    right(40)
    setposition(82,280)
    pendown()
    begin_fill()
    left(130)
    bk(7)
    right(10)
    circle (-20,-50)
    left(10)
    bk(7)                                           ########
    right(110)
    forward(20)                                          ########
    left(60)
    circle (20,90)
    setposition(82,280)
    end_fill()
    penup()                    #*****--------- inside left eye black ----------*****
    setposition(82,280)
    pendown()
    color ("black")
    begin_fill()
    right(6)
    circle (23,-80)
    right(60)
    forward(7)
    left(60)
    circle (23,90)
    setposition(82,280)
    end_fill() 
    penup()                    #*****--------- inside right eye black ----------*****
    setposition(47,280)
    pendown()                            
    begin_fill()
    left(86)
    bk(7)
    right(10)
    circle (-20,-50)
    left(10)
    bk(7)
    left(90)
    forward(7)
    right(80)
    circle (-20,50)
    forward(14)
    right(30)
    forward(7)
    setposition(47,280)
    end_fill()
    penup()                     #*****--------- right blue ----------*****
    setposition(24,276)
    pendown()
    color ("black","skyblue")
    begin_fill()
    circle (7)
    end_fill()
    penup()                     #*****--------- left blue ----------*****
    setposition(93,276)
    pendown()                                 
    begin_fill()
    circle (7)
    end_fill() 
    penup()                     #*****--------- right black ----------*****
    setposition(28,276)
    pendown()
    color ("black")
    begin_fill()
    circle (2.5)
    end_fill()
    penup()                   #*****--------- left black ----------*****
    setposition(97,276)
    pendown()                                     
    begin_fill()
    circle (2.5)
    end_fill()
    penup()                   #*****--------- right white ----------*****
    setposition(29,281)
    pendown()
    pensize(1)
    color ("black","white")
    begin_fill()
    circle (3)
    end_fill() 
    penup()                   #*****--------- left white ----------*****
    setposition(99,281)
    pendown()                                 
    begin_fill()
    circle (3)
    end_fill()
def nose_mouth():
    penup()
    setpos (55,245)
    pendown()
    pensize (3)
    color ("black")
    begin_fill()
    circle (1.5)
    end_fill()
    penup()                     #*****--------- right nose ----------*****
    setpos (70,245)
    pendown()                                
    begin_fill()
    circle (1.5)
    end_fill()
    penup()                     #*****--------- mouth ----------*****
    setpos (35,227)
    color("black","white")
    begin_fill()
    pendown()
    left(38)
    pensize (1.5)
    circle (120,30)
    right(90)
    circle(-10,80)
    right(10)
    circle (-100,30)
    right(10)
    circle(-10,80)
    end_fill()
    penup()
    setposition(35,222)
    pendown()
    right(90)
    circle (120,5)
    penup()
    circle (120,20)
    pendown()
    circle (120,5) 
def line ():
    penup()                                #1                       
    setpos (5,260)
    pensize (2)
    pendown()
    circle (-30,50)                     
    penup()                                #2
    setpos (8,245)
    pendown()
    left(60)
    circle (-30,50)
    penup()                                #3
    setpos (10,230)
    pendown()
    left(65)
    circle (-30,45)        #*****--------- right |<^>| up ----------*****
    penup()                                #1
    setpos (122,260)
    pendown()
    left(175)
    circle (30,50)
    penup()                                #2
    setpos (123,245)
    pendown()
    right(65)
    circle (30,50)
    penup()                                #3
    setpos (118,230)
    pendown()
    right(70)
    circle (30,45)
def ear(): 
   penup()                  #*****--------- right  ----------*****
   setpos (130,298)
   pendown()
   left(50)
   bk(10)
   right(90)
   circle (18,-110)
   left(90)
   forward(10)
   penup()                  #*****--------- left  ----------*****
   setpos (2,292)
   pendown()
   left(9)
   forward(10)
   left(90)
   circle (18,110)
   left(90)
   forward(10) 
def neck():
    penup()
    setpos (13,223)
    color ("#191a1c")
    begin_fill()
    pendown()
    right(120)
    circle (50,30)
    right(17)
    circle (44,90)
    right(17)
    circle (50,37)
    right(85)
    forward(7)
    circle (-5,100)
    left(25)
    forward(20)
def shiright():
    left(132)                 #hand            
    forward(30)
    circle (-120,50)
    left(2.5)                       #handup position
    circle (80,-35)
    bk(115)                   #bend 1 up pos
    left(65)
    circle(40,43)
    right(93)                       #hand down position 
    circle (-1000,10)
    circle (-30,30)           #bend 2 down pos
    right(31)
    circle (-50,50)
    circle (-600,9)
    left(75)                   #*****---------  body ----------*****
    circle (-1150,10)
    circle (-7,80)
    left(4)
    circle (-900,9)             #hip
    forward(55)
    circle (-7,80)
    circle (-1180,9)    
    left(185)                  #*****--------- left hand position down _  ----------*****
    circle (-250,30)
    left(15)
    circle (-7,130)
    left(25)
    circle (-550,10)           # bend 1 up
    right(65)
    circle(-32,60)
    right(35)
    circle (-133,27)          #*****--------- left hand position up -  ----------*****
    left(140)
    circle (-256,20)
    circle (-30,58)
    forward(75)
    left(80)
    forward(17)
    right(30)
    circle (-5,100)
    setpos (13,223)
    end_fill()
def shirt_design():
    penup()                  #*****--------- orange shirt design right ----------*****
    setposition(185,170)
    pensize(1)
    pendown()
    color("#ff7619")
    begin_fill()
    right(62)
    circle(1070,7.5)
    left(50)
    circle(-23,140)
    forward(73)
    circle(-9,90)
    circle(-950,7)
    circle(-9,84) 
    setposition(170,170)   
    end_fill()
    penup()                  #*****--------- orange shirt design left ----------*****
    setposition(-46,155)
    pendown()
    begin_fill()
    right(95)
    circle(1070,7)
    right(50)
    circle(23,136)
    forward(71)
    circle(9,90)
    right(2)
    circle(950,7)
    circle(9,84) 
    setposition(-40,155)
    end_fill()
    penup()                      #*****--------- white shirt line-design ----------*****
    setposition(65,195)
    pendown()
    pensize(2)
    color("white")
    left(90)
    circle(230,9)
    left(23)
    circle(-15,60)
    circle(15,60)
    circle(-25,60)
    circle(20,50)
    circle(-20,50)
    circle(25,60)
    circle(-25,60)
    circle(20,60)
    circle(-20,60)
    left(15)
    circle(155,8)
def leg():
    penup()                #*****--------- hip ----------*****
    setposition(-30,-40)
    color("#ff7619") 
    pendown()
    begin_fill()
    left(90)
    circle (1150,10)
    circle (-3,88)
    circle (-1800,10)     #*****--------- right leg ----------*****
    right(61)
    circle(-40,60)
    right(44)
    circle (1800,7.6)
    circle(4,141)                       #<------ curve----- 
    circle(1800,7.6)      #*****--------- left leg ----------*****
    right(40)
    circle(-40,60)
    right(63)
    circle(-1800,10)
    end_fill()
def left_hand():
    penup()
    setposition(-145,96)
    color ("black","#f4b9a2")
    pensize(1)
    begin_fill()
    pendown()
    left(117)
    circle(32,59)
    right(120)
    forward(45)
    right(130)
    circle(20,35)
    circle(20,-70)           #------------   1st finger   --------
    bk(25)
    left(180)
    circle(-3,180)
    forward(13)
    right(10)                #------------   2nd finger   --------
    bk(21)
    left(180)
    circle(-3,180)
    forward(16)
    right(10)                #------------   3rd finger   --------
    bk(21)
    left(180)
    circle(-3,180)
    forward(21)
    right(10)                 #------------   4th finger   --------
    bk(19)
    left(180)
    circle(-3,180)
    forward(20)
    left(40)                  #------------   5th finger   --------
    circle(8,130)
    circle(-11,60)
    right(250)
    circle(11,-60)
    right(35)                  #------------   hand   --------
    circle(-8,-90)                                           
    circle(14,-110)
    circle(14,30)
    setposition(-145,96)
    end_fill()
def  foot():
    penup()                    #*****---------- right feet -----------*****
    setposition(3,-356)
    color ("#f4b9a2")
    begin_fill()
    pendown()
    right(225)
    circle(-30,60)
    left(114)
    forward(35)
    left(90)
    forward(25)
    setposition(3,-356)
    end_fill()
    penup()                     #*****---------- left feet -----------*****
    setposition(180,-358)
    begin_fill()
    pendown()
    right(155)
    circle(-30,60)
    left(128)
    forward(35)
    left(90)
    forward(25)
    setposition(180,-358)
    end_fill()
def shoes():
    penup()                    # ****-------  left shoe  ----1st circle-----------****
    color("black","#504948")
    right(3)
    setposition(-2,-396)
    begin_fill()
    pendown()
    circle(5,180)
    forward(24)
    left(190)
    circle(-5,-180)    
    setposition(-2,-396)
    end_fill()
    penup()                  # ****----------- 1st -----------****
    setposition(-1,-396)
    begin_fill()
    pendown()
    left(80)
    forward(10)
    right(90)
    forward(25)
    right(90)
    forward(10)
    setposition(-1,-396)
    end_fill()
    penup()                      # ****-----------2nd circle-----------****
    color("black","#504948")
    setposition(-2,-415)
    begin_fill()
    pendown()
    right(90)
    circle(5,180)
    forward(23)
    left(180)
    circle(-5,-180)    
    setposition(-2,-415)
    end_fill()
    penup()                    # ****----------- bottom 1-----------****
    setposition(-28,-415)
    begin_fill()
    pendown()
    left(45)
    circle(130,15)
    circle(18,180)
    right(10)
    circle(130,15)
    left(24)
    forward(17)
    setposition(-28,-415)  
    end_fill()  
    penup()                    # ****----------- bottom 2-----------****
    setposition(2,-429)
    begin_fill()
    pendown()
    left(156)
    circle(-130,20)
    right(12)
    circle(-18,125)
    right(8)
    circle(-21,-130)
    left(12)
    circle(-130,-13)
    setposition(2,-429)
    end_fill()
    penup()                    # ****----------- curve 1-----------****
    setposition(-17,-455)
    color("black")
    pendown()
    left(50)
    circle(-25,-90)
    penup()                    # ****----------- curve 2-----------****
    setposition(-11,-450)
    pendown()
    right(90)
    circle(-25,-90)
    penup()                      # ****------  right shoe  -----1st circle-----------****
    color("black","#504948")
    right(15)
    setposition(177,-396)
    begin_fill()
    pendown()
    circle(5,180)
    forward(24)
    left(190)
    circle(-5,-180)    
    setposition(177,-396)
    end_fill()
    penup()                  # ****----------- 1st -----------****
    setposition(178,-396)
    begin_fill()
    pendown()
    left(80)
    forward(10)
    right(90)
    forward(25)
    right(90)
    forward(10)
    setposition(178,-396)
    end_fill()
    penup()                      # ****-----------2nd circle-----------****
    color("black","#504948")
    setposition(177,-415)
    begin_fill()
    pendown()
    right(90)
    circle(5,180)
    forward(23)
    left(180)
    circle(-5,-180)    
    setposition(177,-415)
    end_fill()
    penup()                    # ****----------- bottom 1-----------****
    setposition(180,-415)
    begin_fill()
    pendown()
    right(45)
    circle(130,-15)
    circle(18,-180)
    left(10)
    circle(130,-15)
    right(24)
    bk(17)
    setposition(180,-415)  
    end_fill()  
    penup()                    # ****----------- bottom 2-----------****
    setposition(151,-429)
    begin_fill()
    pendown()
    left(23)
    circle(130,20)
    left(15)
    circle(18,125)
    left(8)
    circle(21,-130)
    right(23)
    circle(-130,-13)
    setposition(151,-429)
    end_fill()
    penup()                    # ****----------- curve 1-----------****
    setposition(170,-455)
    color("black")
    pendown()
    right(60)
    circle(25,-90)
    penup()                    # ****----------- curve 2-----------****
    setposition(163,-450)
    pendown()
    left(90)
    circle(25,-90)
    penup()                   # ****----------- left leg  finger -----------****
    setposition(-17,-455)
    color("black","#f4b9a2")
    begin_fill()
    pendown()
    left(115)
    circle(-25,-85)
    right(120)
    forward(11)
    circle(2,180)          # ****----------- left leg 1st finger -----------****
    forward(8)
    bk(11)
    circle(-2.2,-175)       # ****----------- left leg 2nd finger -----------****
    bk(11)
    forward(13)
    circle(2.4,180)         # ****----------- left leg 3rd finger -----------****
    forward(13)
    bk(15)
    circle(-2.6,-175)       # ****----------- left leg 4th finger -----------****
    bk(15)
    forward(16)
    circle(4.3,165)         # ****----------- left leg 5th finger -----------****
    setposition(-17,-455)
    end_fill()
    penup()                    # ****----------- right leg finger -----------****
    setposition(167,-455)
    begin_fill()
    pendown()         
    right(145)
    circle(25,-85)
    left(125)
    forward(11)
    circle(-2,180)          # ****----------- right leg 1st finger -----------****
    forward(8)
    bk(11)
    circle(2.2,-175)       # ****----------- right leg 2nd finger -----------****
    bk(11)
    forward(13)
    circle(-2.4,180)         # ****----------- right leg 3rd finger -----------****
    forward(13)
    bk(15)
    circle(2.6,-175)       # ****----------- right leg 4th finger -----------****
    bk(15)
    forward(16)
    circle(-4.3,165)         # ****----------- right leg 5th finger -----------****
    setposition(167,-455)
    end_fill() 
    penup()                    # ****----------- left nail -----------**** 
    setposition(-30,-462)
    pendown()
    circle(2)
    penup()                    # ****----------- right nail -----------****
    setposition(187,-460)
    pendown()
    circle(2)
def leg_band():
    penup()                    # **********--------- white strap ---------**********
    color("black","white")
    begin_fill()
    setposition(67,-145)
    left(30)
    pendown()
    forward(105)
    left(93)
    forward(50)
    left(90)
    forward(90)
    setposition(67,-145)    
    end_fill()
    setposition(-38,-156)                 # **********--------- white strap line 1 ---------**********
    setposition(60,-167)                  # **********--------- white strap line 2 ---------**********
    setposition(-38,-178)                # **********--------- white strap line 3 ---------**********
    setposition(55,-190)                 # **********--------- white strap line 4 ---------********** 
    penup()                                        # ***--------- box strap ---------*** 
    setposition(63,-161)
    color("black","#504948")
    pensize(2)
    begin_fill()
    pendown()
    bk(100)
    right(90)
    forward(10)
    left(90)
    forward(95)
    setposition(63,-161)
    end_fill()
    penup()                      # ***--------- box ---------*** 
    setposition(-48,-131)
    begin_fill()
    pendown()
    right(90)
    forward(70)
    left(90)
    forward(16)
    left(90)
    forward(70)
    setposition(-48,-131)
    bk(10)
    right(105)
    forward(15)
    end_fill()
def rasengan():
    penup()
    setposition(-215,248)
    pendown()
    pensize(0.6)
    color("white","light skyblue")
    begin_fill()
    for i in range(55):
        circle(i*0.5)
        right(170)
        circle(i*0.5)
        right(170)
        circle(i*-1)
        right(170)
        penup()
        circle(i*-1)
        right(170)
        circle(i*-1)
        right(170)
        pendown()
        circle(i*-1)
        right(170)
    end_fill()    
#*************------````~~~~~~~````--------------- Functions ---------------````~~~~~~~````------*************
font()
hair()
head_band()
face()
eyebrow()
bandhair()
eye()
nose_mouth()
line()
ear()
neck()
shiright()
shirt_design()
leg()
left_hand()
foot()
shoes()
leg_band()
rasengan()
done()