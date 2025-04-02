# # Variables
fullName = "Benedicta"
age = 5
location = "Harare"

print(fullName)
print(age)
print(location)

print("You are favoured")

# data types
continent = "Africa"
print(type(continent))

x = 5
y = 9
print(f"addition {x + y}")
print(f"subtraction {x - y}")
print(f"mutltiplication {x * y}")
print(f"division {x / y}")
print(f"integer division {x // y}")
print(f"modulus {x % y}")
print(f"expo or power of {x ** y}")

num_of_fruits = 25
print(type(num_of_fruits))

num_of_fruits = 25.5
print(type(num_of_fruits))

# boolean
7 == 7 
print(7 == 7)

4 < 2
print(4 < 2)

28 >= 28
print(28 >= 28)

29 > 2
print(29 > 2)

55 <= 55
print(55 <= 55)

56 == 56 
print(56 == 56)

2 >= 2 
print(2 >= 2)

29 > 56
print(29 > 56)

45 <= 2
print(45 <= 2)

10<5
print(type(10<5))

# lists
names = ["Belle", "Anna", "Katie", "Samantha"]
print(names)

nums = [2, 4, 6, 8, 10,]
print(nums)

mixedList = ["Katie", 10, 8.5, [1, 2, 3, 4, 5], False]
print(mixedList)

# accessing items in a list
print(names[2])
print(nums[0])
print(mixedList[-2])

# list slicing
print(names[1:3])
print(nums[:4])
print(mixedList[1:])
print(mixedList[1:-1])

# modifying a list
nums = [2, 4, 6, 8, 10,]
nums[2] = 5
print(nums)

nums = [2, 4, 6, 8, 10,]
nums.append(12)
print(nums)

nums = [2, 4, 6, 8, 10,]
nums.insert(3, 25)
print(nums)

nums = [2, 4, 6, 8, 10,]
nums.remove(6)
print(nums)

names = ["Belle", "Anna", "Katie", "Samantha"]
names.pop(1)
print(names)

names = ["Belle", "Anna", "Katie", "Samantha"]
names.clear()
print(names)

mixedList = ["Katie", 10, 8.5, [1, 2, 3, 4, 5], False]
del mixedList[3]
print(mixedList)

mixedList = ["Katie", 10, 8.5, [1, 2, 3, 4, 5], False]
del mixedList[2]
print(mixedList)

# Dictionary
student = {
    "name" : "Benedicta",
    "age" : 5,
    "gender" : "female"
}
print(student)
print(student["age"])

# get method
print(student.get("country"))

# modifying a dict
student = {
    "name" : "Benedicta",
    "age" : 5,
    "gender" : "female"
}
student["name"] = "Phiri"
print(student)

student["gender"] = "rather not say"
print(student)

student.update({"country": "Zimbabwe", "city": "Harare"})
print(student)

student.update({"phone": "+263786236945"})
print(student)

student.update({"food": "apple"})

del student["gender"]
print(student)

student.clear()
print(student)

# tuples
my_tuple = ("apple", "banana", "cherry", 5, 10)
print("Tuple:", my_tuple)

#accessing tuple elements
print("first element of the tuple:", my_tuple[0])
print("last element of the tuple:", my_tuple[-1])

#slicing a tuple
sliced_tuple = my_tuple[1:4]
print("sliced tuple(from index 1 to 3):",sliced_tuple)

#check if elements are in a tuple
if "banana" in my_tuple:
    print("banana is in the tuple!")

#sets
my_set = {"apple", "banana", "orange", "banana", "apple",}
print(my_set)

#adding items to sets
my_set.add("2sep")
print("set after adding date:", my_set)

#removing elements
my_set.remove("banana")
print("set after removing banana:", my_set)

#discarding elements
my_set.discard("cherry")
print("set after discarding cherry:", my_set)

#union of sets
set = {"orange", "grape", "apple"}

union_set = my_set.union(set)
print("intersection of sets:", my_set)

#difference of sets
difference_set = my_set.difference(set)
print("difference of sets:",difference_set)

# conditional statements
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

x = 2
if x > 5:
   print(f"{x} is equal to 5")
else:
   print(f"{x} is less than 5")

name = "admin"
password = 1234

if name == "admin" and password == 1234:
   print(f"welcome {name}")
else: 
   print(f"invalid password")

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
   print("wear overalls")

# logical operators
x = True
y = False
print(x and y)

x = True
y = False
print(x or y)

x = True
y = False
print(not x)

#loops
#while loops

l = 4
while l < 20:
     print(l)
     l = l + 1


i = 0
while i < 10:
      print(i)
      i = i + 1

num = 20
while num < 20:
    print(num)
num = int (input("Enter number: "))
if not num == 20:
    print("you guessed right")
else:
    num = int (input("Enter number: "))
print("you guessed right")

answer = 100
guess = int(input("Guess a number: "))

while guess != answer:
    print("wrong answer")
    guess = int(input("Wrong Number! Guess again: "))

print("You guessed the right number!😊")

answer = 6
guess = int(input("Guess a number: "))

while guess != answer:
    print("Wrong answer")
    if guess < answer:
        print("Your number is less than the expected number.")
    else:
        print("Your number is greater than the expected number.")
    guess = int(input("Guess again: "))

print("You guessed the right number! 😊")
        
# for loops
# looping through a list
fruits = ["cherry", "apple", "coconut",]
for fruit in fruits:
    print(fruit)

# looping through a string
text = "Benedicta"
for char in text:
    print(char)

def greet():
     print("Hello, welcome to Zimbabwe!")
greet()

def greet(name):
     print(f"Hello, {name}!")
greet("Kaile")
greet("Zoe")

def add(a,b):
    return a + b
result = add(10,5)
print(result)

def subtract(a,b):
    return a - b
result = subtract(20,6)
print(result) 

def multiply(a,b):
    return a * b
result = multiply(2,10)
print(result)

def divide(a,b):
    return a/b
result = divide(10,5)
print(result)

def power(base, exponent):
    return base ** exponent
print(power(7,6))

def greet(name):
    print(f"Hello, {name}")
greet("Benedicta")

def multiply(a, b):
    return a * b

print(multiply(6,9))

result = multiply(6,9)
print(result)
