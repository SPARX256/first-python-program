# my_tuple = ("apple", "banana", "cherry", 5, 10)
# print("Tuple:", my_tuple)

# #accessing tuple elements
# print("first element of the tuple:", my_tuple[0])
# print("last element of the tuple:", my_tuple[-1])

# #slicing a tuple
# sliced_tuple = my_tuple[1:4]
# print("sliced tuple(from index 1 to 3):",sliced_tuple)

# #my_tuple[0] = "orange"

# #check if elements are in a tuple
# if "banana" in my_tuple:
#     print("banana is in the tuple!")

# #sets
# my_set = {"apple", "banana", "orange", "banana", "apple",}
# print("\nset:", my_set)

# #adding items to sets
# my_set.add("2sep")
# print("set after adding date:", my_set)

# #removing elements
# my_set.remove("banana")
# print("set after removing banana:", my_set)

# #discarding elements
# my_set.discard("cherry")
# print("set after discarding cherry:", my_set)

# #union of sets
# set = {"orange", "grape", "apple"}

# union_set = my_set.union(set)
# print("intersection of sets:", my_set)

# #difference of sets
# difference_set = my_set.difference(set)
# print("difference of sets:",difference_set)

# #Set_is_unordered:order may change
# #print("\nFinal set:", my_set)

# #a,b,c,d,e = my_tuple
# #print("\nunpacked tuple:",a,b ,c,d,e)

# nested_tuple = (("apple", "banana"),(1,2,3))
# print("nested tuple:",nested_tuple)

# students = ("jon", "jane", "peter", "james", "mary", "john", "matt", "vin", "anna")
# #print(students[1:-1:3])
# print(students[ : :2])
# # [start:stop:step]


# tup1 = (1, 2, 3, 4, 5)
# tup2 = (6, 7, 8, 9, 10)

# print(tup1 + tup2)
# print(tup1)
# print(tup2)
# print(tup1 * 2)

# tup3 = (6, 7, 8, 9, 10)
# print(len(tup3))

# my_list = list(tup3)
# print(my_list)

# list2 = [1, 2, 3, 4, 5]
# my_list.extend(list2)
# print(my_list)
# #my_list = tuple(my_list)
 
# my_list.sort
# print(my_list)

#Sort numbers from largest to smallest
#sorted_numbers = sorted(numbers, reverse=True)

#print("Sorted numbers (largest to smallest):", sorted_numbers)

# my_list.sort(reverse = True) 
# print(my_list)

#sets
my_set = {1, 2, 3, 4, 5}
#print(my_set)
print("Set:", my_set)
print(type(my_set))

my_set is [1, 2, 3, 4, 5]
#print(f"my set is: {my_set}")
my_set2 = {6, 7, 8, 9}

#union
#union_set = my_set | my_set2
#print(union_set)

my_set.add(25)
print(my_set)

#intersection
int_set = my_set.intersection(my_set2)
int_set = my_set & my_set2
print(int_set)