#This is a toy written to test a Micropython interpreter on a Casio 9860 GIII
# calculator.  It was written on the calculator, with the calculator keyboard,
# but comments were added later with a real keyboard.  It will generate a 
# simple Mandelbrot fractal, in ASCII because there's no facility in the 
# calculator for generating actual graphics from Python.
#
# The calculator also only offers two Python modules, math and random.  This
# uses neither of them.


#In characters.   For the calculator display, a 22x22 square is about as
# good as you can do.  For a terminal, something more reasonable like 80x50
# will give you a better image.
width=80
hight=50

#This is the bounding box for our display.  You might also consider top/bottom,
# and left/right to be sets of boundaries for the imaginary and real parts of
# our complex coordinate, respectively.
left=-1.5
right=.5
top=.9
bottom=-.9

#Beyond this number of iterations, we assume the Z value will eventually be 
# infinity, and is out of the set.
max=60

#This both determines the bucket into which a certain coordinate should be
# placed, and gives back an ASCII character that represents it on the display.
def mdb(n):
  z=0
  i=0
  while abs(z) <= 2 and i < max:
    z=z**2+n
    i=i+1
  if abs(z) >= .5:
    return " "
  if abs(z) >= .4:
    return "*"
  if abs(z) >= .3:
    return "x"
  if abs(z) >= .2:
    return "+"
  return "-"

#The width and height of the fractal field
mw=right-left
mh=bottom-top

#Note that for each character, we calculate a coordinate within the field.
# We run mdb on that.
for y in range(1,hight):
  for x in range(1,width):
    xl=left+((mw/width)*x)
    yl=top+((mh/hight)*y)
    #Our y axis is the imaginary component, and x is the real component.
    print(mdb(complex(xl,yl)),end="")
  print()
  
  
