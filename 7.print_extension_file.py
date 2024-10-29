#7. Write a Python program that accepts a filename from the user and prints the extension of the file.Sample filename : abc.java,    Output : java
#str.split(sep=None, maxsplit=-1)
#Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).

#Note: If maxsplit is specified, the list will have a maximum of maxsplit+1 items.
filename = input("Input the file name: ")
f_extension = filename.split(".")
# Print the extension of the file, which is the last element in the 'f_extns' list
print("The extension of the file is : " , repr(f_extension[-1]))

#The repr() function returns a printable representation of the given object.