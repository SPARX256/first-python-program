# conditional statements
register = 'prsent'
name = 'Benedicta'

if register == 'present':
   print(f"{name} is {register}")
else:
   print(f"{name} is absent")
 
x = 2
if x > 5:
   print(f"{x} is equal to 5")
else:
   print(f"{x} is less than 5")

condition = "sunny"
# question 
# Write a program that asks for a username and pass if the name is "admin" and the password is "1234" 
# Print "Welcome admin" else print "Invalid username or password"

name = "admin"
password = 1234

if name == "admin" and password == 1234:
   print(f"welcome {name}")
else: 
   print(f"invalid password")

name = input("Enter your name:")
print(name)

num1 = input("Enter the first number:")
num2 = input("Enter the second number:")

result = num1 + num2
print(result)

num1 = "23"
num2 = int(num1)
print(type(num2))

num1 = int(num1)
num2 = int(num2)
result = num1 + num2
print(result)
print(type(result))

num1 = float(num1)
num2 = float(num2)
result = num1 + num2
result = str(result)
print(result)
print(type(result))

a = 25
b  = 24
c = 2

print(a > b and b == c)

username = "admin"
password = 1234
# welcome admin you are logged in #  
# invalid credentials #false

username = "admin"
password = 1234

username = input('Enter your username:')
password = int (input('Enter your password:'))

if username == "admin" and password == int (1234):
   print(f"welcome {username} you are logged in")
else:
   print(f"invalid credentials")


temp = int(input('Enter temp: '))
condition = "sunny"
if temp >= 30 and condition == "sunny":
   print(f"the temp is {temp} degrees and it is {condition}")
else:
   print("it is cold")

day = input("Enter day: ")

day = "MONDAY"
print(day.lower())

days = ("monday", "tuesday", "wednesday", "friday")

day = input("Enter day: ").lower()

if days in days:
    print(days)
else:
    print:(f"not correct") 

if day == "monday":
   print("wear uniform")
elif day == "tuesday": 
   print("wear garments")
elif day == "wednesday":
   print("wear casual")
elif day == "thursday":
   print("wear formal")
else:
   print()

grade = ("A, B, C, D , F")
score = (input("Enter the student's score (0-100): "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

