# a function is a block of code that
# we need functins for: 
# reduce code duplication
# organization of data\code
# easy debugging and maintanance
# parameters allow functions to call an input

# Syntax:
# def function name (parameters):
    # function board
    # return a value

# def greet():
#     print("Hello, welcome to Python!")
# greet()

# def greet(name):
#     print(f"Hello, {name}!")
# greet("Benedicta")
# greet("Phiri")

# def add(a,b):
#     return a + b
# result = add(2,3)
# print(result)

# def subtract(a,b):
#     return a - b
# result = subtract(2,3)
# print(result) 

# def multiply(a,b):
#     return a * b
# result = multiply(2,3)
# print(result)

# def divide(a,b):
#     return a/b
# result = divide(2,3)
# print(result)

# positional arguements
# arguments are assigned in their order
# def power(base, exponent):
#     return base ** exponent
# print(power(2, 3))

# default arguments
# def greet(name):
#     print(f"Hello, {name}")
# greet("Benedicta")

# def greet(name = "Guest"):
#     print(f"Hello, {name}")
# greet()

# def multiply(a, b):
#     return a * b

#  print(multiply(5,7))

# result = multiply(5,7)
# print(result)

# nested functions
# def outer():
#     print("This is outer function")
#     def inner():
#         print("This is inner function")
#     outer()    
#     inner()
# outer()

# def global_function():
#     print("This is a global function")
# global_function()

# def another_function():
#     global_function()
# another_function()    
