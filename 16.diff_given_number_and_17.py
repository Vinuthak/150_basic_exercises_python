#16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
'''
given_number = int(input("Enter a number: "))
if(given_number<= 17):
  print("The difference is ",17-given_number)
else(given_number>17):
  print("The difference is ", (given_number-17)*2)

'''

def difference(n):
  if n <= 17:
    return 17 - n
  else: 
    return (n-17)*2

print(difference(10))
print(difference(20))


 