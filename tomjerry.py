from turtle import*
import turtle
from time import*
turtle.screensize(750,680)
bgcolor ("black")
speed (5)
penup()

def tom():
   setposition(-45,-340)
   color ("white","#4b6d9a")
   begin_fill()
   pendown()
   right(30)
   backward(175)
   circle (120,-150)
   right(0)
   circle (-170,50)
   right(45)
   backward(50)
   left(40)
   circle (-89,40)
   right(20)
   backward(50)
   left(55)
   circle (-89,50)
   left(60)
   forward(40)
   right(80)
   circle (-50,40)
   left(60)
   forward(25)
   
#ear         ****************************************************************
  
   right(-55)
   circle (-80,50)
   right(10)
   circle (170,35)
   circle (50,30)
   left(50)
   circle (160,-65)
   right(70)
   circle (-130,30)

#      **************************************************************************
   
   right(30)
   backward(40)
   circle (-17,-40)
   right(-30)
   circle(-40,40)
   left(20)
   circle (-30,70)
   right(40)
   circle (40,-90)
   left(40)
   circle (30,135)
   right(100)
   penup()
   forward(640)
   pendown()
   end_fill()
   penup()

#jerry     **************************************************************

def jerry():
   setposition(-45,-340)
   color ("white","#faa505")
   begin_fill()
   pendown()
   right(63.99)
   backward(200)
   circle (-120,-140)
   left(15)    
   forward(30)
   right(-22)
   circle (81,120)
   forward(20)
   backward(15)
   right(140)
   circle (120,130)
   circle (80,60)
   circle (120,60)
   right(105)
   circle (300,5)
   left(150)
   circle (50,-80)
   left(310)
   circle (70,70)
   right(45)
   circle (-30,57)
   end_fill()
   penup()
   hideturtle()

#face    *****************************************************************

def face():
   speed (11)
   pensize(1)
   setposition(-44,90)
   color ("black","#d1e4eb")
   begin_fill()
   pendown()
   left(38)
   forward(80)
   right(90)
   forward(90)    #********************************************************  
   speed(9)
   circle(-20,155)
   left(160)
   circle(-60,75)
   penup()
   setposition(-45,90)
   pendown()
   end_fill()
   penup()
   
#mouth    **************************************************************

def mouth():
   speed (11)
   right(68)
   setposition(-165,20)
   color ("black","white")
   pendown()
   begin_fill()
   circle (170,100)
   right(50)
   circle (30,-180)
   right(40)
   circle (138,60)
   right(40)
   circle (120,60)
   right(45)
   circle (30,-180)
   end_fill()
   penup()

   #nose   ***************************************************************

   setposition(-70,110)
   color ("black")
   pendown()
   begin_fill()
   right(40)
   circle (40,95)
   left(87)
   circle (40,95)
   end_fill()
   penup()
  
   #      ***************************************************************
   
   pensize (3)
   color ("floralwhite")
   begin_fill()
   setposition(-45,107)
   pendown()
   right(235)
   circle(3)
   end_fill()
   penup()
   
#mouth   ****************************************************************

   pensize (4)
   setposition(-40,105)
   color ("black")
   pendown()
   begin_fill()
   right(94)
   forward(70)
   right(40)
   circle (-40,90)
   left(160)
   circle (40,110)
   right(95)
   circle (40,110)
   left(160)
   circle (-40,90)
   right(30)
   forward(70)
   end_fill()
   penup()
 
   setposition(-73,-5)
   pendown()
   left(40)
   circle (-50,-80)
   penup()
   
#eye tom     *************************************************************

def tomeye():
   speed(9)
   setposition(-105,118)
   color ("black","white")
   begin_fill()
   pendown()
   right(138)
   circle (80,50)
   circle (30,90)
   circle (80,90)
   right(70)
   circle (40,-40)
   left(25)
   circle (70,-48)
   end_fill()
   penup()

   setposition(-108,118)
   color("black")
   begin_fill()
   pendown()
   right(100)
   circle (70,30)
   circle (25,120)
   circle (70,70)
   right(70)
   circle (30,-40)
   left(38)
   circle (60,-35)
   end_fill()
   penup()

   setposition(-134,148)
   color ("white")
   begin_fill()
   pendown()
   circle (5)
   end_fill()
   penup() 
   
#eye jerry   ************************************************************
def jerryeye():
   setposition(95,82)
   color ("black","white")
   begin_fill()
   pendown()
   right(151)
   circle (80,80)
   circle (30,90)
   circle (80,70)
   right(100)
   circle (40,-30)
   left(25)
   circle (70,-45)
   end_fill()
   penup()

   setposition(85,95)
   color("black")
   begin_fill()
   pendown()
   right(80)
   circle (70,60)
   circle (20,100)
   circle (70,60)
   right(90)
   circle (30,-40)
   left(38)
   circle (60,-35)
   end_fill()
   penup()

   setposition(70,152)
   color ("white")
   begin_fill()
   pendown()
   circle (5)
   end_fill()
   penup()


#mesai      ****************************************************************

def tommesai():
   pensize(2)
   speed (8)
   setposition(-100,45)
   color ("black")
   pendown()
   left(10)
   circle(100,60)
   penup()

   setposition(-100,55)
   color ("black")
   pendown()
   right(65)
   circle(100,60)
   penup()

   setposition(-100,65)
   color ("black")
   pendown()
   right(65)
   circle(100,60)
   penup()

#                ****************************************************************

def jerrymesai():
    
   setposition(20,40)
   color ("black")
   pendown()
   left(5)
   circle(100,-60)
   penup()

   setposition(20,50)
   color ("black")
   pendown()
   left(65)
   circle(100,-60)
   penup()

   setposition(20,60)
   color ("black")
   pendown()
   left(65)
   circle(100,-60)
   penup()
   
#ear tom    ****************************************************************

def tomear():
   speed(10)
   pensize(1)
   right(85)
   setposition(-287,138)
   pendown()
   color ("hotpink")
   begin_fill()
   right(-55)
   circle (-80,50)
   right(10)
   circle (170,35)
   circle (50,30)
   left(25)
   circle (160,-65)
   left(130)
   forward(30)
   left(100)
   circle (20,-90)
   right(30)
   circle (20,90)
   circle (-20,-90)
   right(200)
   circle (20,-90)
   setposition(-287,138)
   end_fill()
   
#ear jerry  ***************************************************************

def jerryear():
   penup()
   setposition(165,134)
   pendown()
   begin_fill()
   right(85)
   circle (100,130)
   circle (70,60)
   circle (100,60)
   left(30)
   forward(20)
   left(50)
   circle (80,50)
   left(30)
   circle (80,-30)
   setposition(165,134)
   penup()
   end_fill()
   penup()

#eye brows tom   *********************************************************

def tom_eye_brow():
   speed(5)   
   color ("black")
   pensize (6)
   setposition(-185,205)
   pendown()
   right(160)
   circle (40,-90)
   penup()

#eye brows Jerry   ********************************************************

def jerry_eye_brow():
       
   color ("black")
   pensize (6)
   setposition(55,205)
   pendown()
   left(-260)
   circle (40,-90)
   penup()

#heart    ******************************************************************

def heart():
   speed (3)
   setposition(-45,-330)
   pendown()
   right(123)
   color ("red","#8b0000")
   begin_fill()
   forward(150)
   circle (112,205)
   right(95)
   circle (110,175)
   setposition(-45,-330)
   end_fill()
   penup ()
    
def font():
   setposition(-180,-140)
   pendown()
   sleep(.30)
   color ("gold","black")
   write ("T",font=("courier",40,"bold")) 
   penup () 

   setposition(-140,-140)
   pendown()
   sleep(.30)
   write ("o",font=("courier",40,"bold")) 
   penup () 

   setposition(-100,-140)
   pendown()
   sleep(.30)
   write ("m",font=("courier",40,"bold"))
   penup () 

   setposition(-130,-195)
   pendown()
   sleep(.30)
   write (" a",font=("courier",40,"bold"))
   penup ()  

   setposition(-60,-195)
   pendown()
   sleep(.30)
   write ("n",font=("courier",40,"bold"))
   penup () 

   setposition(-20,-195)
   pendown()
   sleep(.30)
   write ("d ",font=("courier",40,"bold"))
   penup ()  

   setposition(-100,-260)
   pendown()
   sleep(.30)
   write (" J",font=("courier",40,"bold")) 
   penup () 

   setposition(-30,-260)
   pendown()
   sleep(.30)
   write ("e",font=("courier",40,"bold")) 
   penup () 

   setposition(10,-260)
   pendown()
   sleep(.30)
   write ("r",font=("courier",40,"bold")) 
   penup () 

   setposition(50,-260)
   pendown()
   sleep(.30)
   write ("r",font=("courier",40,"bold"))
   penup ()  

   setposition(90,-260)
   pendown()
   sleep(.30)
   write ("y",font=("courier",40,"bold")) 
   hideturtle()


tom()
jerry()
face()
mouth()
tomeye()
jerryeye()
tommesai()
jerrymesai()
tomear()
jerryear()
tom_eye_brow()
jerry_eye_brow()
heart ()
font()

done ()

#arial
#verdana
#courier
# calibri
#Time New Roman
#Apple Chancery
# Helvetica
# Comic Sans MS    ----------- 1  
# Impact
# Georgia          -----------2
# Tahoma
# Trebuchet MS
# Lucida Sans Unicode
#  Fixedsys
# Times              ---------3
# Palatino           ---------4
# Lucida console 
# Cooper Black


#f0cece