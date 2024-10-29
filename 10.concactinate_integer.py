# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615

value = int(input("Enter a number: "))
n1 = int("%i" %value)
n2 = int("%i%i" %(value,value ))
n3 = int("%i%i%i" %(value,value,value ))
print("The result is ", n1+n2+n3)