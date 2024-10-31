#18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
def sum_of_three_numbers(a,b,c):
  if(a == b == c):
    result = 3*(a+b+c)
  else:
    result = a + b + c
  return result    

print(sum_of_three_numbers(a,b,c))