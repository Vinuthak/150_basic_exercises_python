#Write a  Python program to print the documents (syntax, description etc.) of Python built-in function(s).
#Sample function: abs()

'''
  Docstrings: These are essential documentation strings in Python that describe the purpose and usage of modules, functions, classes, or methods. The docstring is available through the "doc" attribute.
Built-in Functions: Python provides many built-in functions such as abs(), len(), sorted(), sum(), map(), filter(), etc. Each function has a corresponding docstring that describes its usage.
'''

#A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object.

#All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods (including the __init__ constructor) should also have docstrings.


print(abs.__doc__)
print(map.__doc__)
