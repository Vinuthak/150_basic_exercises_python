#6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers 
# Sample data : 3, 5, 7, 23

numbers = input("Enter a list of numbers: ")
#A sequence of numbers taken from input cannot be converted to int,a single number can be converted

list = numbers.split(',')


tuple = tuple(list)
print("Numbers in list: ",list)

print("Numbers in tuple: ",tuple)


#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple. In the same way a tuple also converts a sequence of intergers with comma.