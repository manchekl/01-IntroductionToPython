"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Krista Manche.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
blue_turtle=rg.SimpleTurtle('turtle')
blue_turtle.pen=rg.Pen('blue',2)
blue_turtle.speed=100

pink_turtle=rg.SimpleTurtle('turtle')
pink_turtle.pen=rg.Pen('pink',5)
pink_turtle.speed=3

for k in range(200):
    blue_turtle.right(50)
    blue_turtle.forward(k)
    blue_turtle.left(10)

pink_turtle.left(20)
for k in range (9):
    pink_turtle.forward(300)
    pink_turtle.pen_up()
    pink_turtle.go_to(rg.Point(0,0))
    pink_turtle.left(40)
    pink_turtle.pen_down()

window.close_on_mouse_click()
