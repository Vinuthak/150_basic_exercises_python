#Write a Python program that calculates the area of a circle based on the radius entered by the user
from math import pi
radius = float(input("Enter the radius: "))
def radius_of_a_circle(radius):
  area = pi*(radius**2)
  print(area)
  return area
radius_of_a_circle(radius)