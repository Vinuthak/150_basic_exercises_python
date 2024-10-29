# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
def name():
  first_name = input("Enter first name: ")
  last_name = input("Enter last name: ")
  order = "Hello " + last_name + " " + first_name
  print(order)

name()