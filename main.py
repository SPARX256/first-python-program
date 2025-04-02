print("Welcome to mufakose")
score = 0
full_name = "Benedicta Phiri"

print(score)
print(full_name)

country = "Zimbabwe"
time = 30
phone_number = "0786236945"

print(country)
print(time)
print(phone_number)

print("My name is 1234")

city = "harare" 
print(type(city)) # this expression is printing the data type of the variable city

#integer types
number_of_pupils = 40
print(type(number_of_pupils))

#float types
number_of_pupils = 40.567
print(number_of_pupils )
print(type(number_of_pupils))

x = 15
y = 5
print(f"addition {x + y}")
print(f"subtration {x - y}")
print(f"multiplication {x * y}")
print(f"division{x / y}")
print(f"integer division {x // y}")
print(f"modulus {x % y}")
print(f"expo or power of {x ** y}")

# operators
# +, -, /, *, //, %,**

# boolean => it returns true or false
# boolean comparison operators
# != means not equal to
# < greater than
# > less than
# <= greater than or equal to 
# >= less than or equal to

print(10<5)
print("results")
print(7<=7)
print("results")

# list is a collection of items used to store multiple items in a single variable
# lists are ordered, changed and indexed
# lists are denoted by square brackets
# lists are mutable
# lists are ordered collection of items

fruits = ["apple", "banana", "cherry", "orange", "mango"]
numbers = [10, 9, 3, 4, 5, 6, 7, 8, 9, 10]
mixedList = [True, 1, 2.0, "sama", [1, 2, 3]]

print(fruits)
print(numbers)
print(mixedList)

# accessing items in a list
# indexing to index an element we use +ve & -ve to accss items in a list
# first item is represented by 0
# +ve index starts from 0 (this is the first item)

fruits = ["apple", "cherry", "orange"]

print(fruits[0])
print(fruits[-1])

# list slicing
# when we slice a list we use start & end
# list [start:end]


numbers = [10, 20, 30, 40, 50]
print(numbers)
print(numbers[1:4 ])
print(numbers[-2])

# modifying a list

numbers = [10, 20, 30, 40, 50]
numbers[0] =5
print(numbers)

# adding items in a list, append & insert
# append, the item goes to the end of the list
# insert, the item goes at a specific index

fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)
fruits.insert(1, "mango")
print(fruits)

# removing items we have, remove, pop, del and clear
# remove removes a specific item
# pop removes the first item
# del deletes the entire list
# clear empties the entire list

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.pop(0)
print(fruits)

fruits = ["apple", "banana", "cherry"]
del fruits[-1]
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

# Dictionary
# a dictionary is a collection that stores key value pairs,
# we separate key and value with a colon (:)
student = {
   "name" : "Bene",
   "age" : 2,
   "grade" : 2
}
print(student)
print(student["name"])
#print(student["country"])

#get method
print(student.get("country"))

# modify a dictionary
student = {
   "name" : "Bene",
   "age" : 2,
   "grade" : 2
}
student["name"] = "Zoe"
print(student)

student["age"] = 45
print(student)

student.update({"country": "Zimbabawe", "city": "Harare"})
print(student)

student.update({"phone": 1234567890, "address": "1234 Main st"})
print(student)

del student["phone"]
print(student)




