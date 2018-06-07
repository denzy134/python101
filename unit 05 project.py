import math

print("This calculator solves three equations\n")
response = (input('Enter input in Caps. Enter C for Circle, T for triangle or R for rectangle = '))

def areaCircle(radius):
    area = (math.pi * radius * radius)
    return area
   
def areaTriangle(base,height):
    areaT =  (0.5 * base * height)
    return areaT

def areaRectangle(width,height3):
    areaR = width * height3
    return areaR
    
if response == "C":
  radius = float(input('Enter radius = '))
  area = areaCircle(radius)
  print ('Area of the circle = ' ,area)
elif response == "R":
  width = float(input('Enter width : '))
  height3 = float(input('Enter height : '))
  areaR = areaRectangle(width,height3)
  print ('Area of rectangle = ',areaR)
elif response == "T":
  base = float(input('Enter base : '))
  height = float(input('Enter height : '))
  areaT = areaTriangle(base,height)
  print ('Area of triangle = ' ,areaT)
else:
  print ("invalid option")

