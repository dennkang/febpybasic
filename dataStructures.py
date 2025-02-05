# List Data Structure
# They are mutable, ordered and indexed

fruits = ['apple', 'banana', 'orange']

print(fruits)

print(f"I would like an {fruits[0]}.")

# replace value in fruits
fruits[0] = 'pear'

print(fruits)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers)

# add a new value to list
numbers.append(11)

print(numbers)

numbers2 = [92,-39,21,18,-44,59,-61,5,19,26]

print(numbers2)

# sort lists
numbers2.sort()
print(numbers2)

numbers2.sort(reverse=True)
print(numbers2)

print("")
# tuples
# they are ordered, indexed and immutable

cars = ("Alpha Romeo", "Bentley", "Chevrolet", "Dodge")

print(cars)

# tuples are ordered
print(f"He drives a brand new {cars[0]}")

# tuple cannot relace values
# cars[0] = "Audi"
# print(cars)

# tuple cannot add new value
# cars.append("Ferarri")
# print(cars)

# tuple sort
print(sorted(cars))

print("")

nambari = (73,28,-13,62,31,-8,98,97,-9,25,-33)
print(nambari)

print(sorted(nambari))

print("")
# sets
# They are unordered, not indexed

computers = {'hp', 'dell', 'lenovo', 'acer', 'mac', 'toshiba', 'ibm'}
print(computers)

# adding items
computers.add('asus')
print(computers)

# remove items
computers.remove('ibm')
print(computers)

num1 = {1,2,3}
num2 = {4,5,6}

# combine sets
union_set = num1.union(num2)
print(union_set)

print("")

# dictionaries

students = {'Name': 'Jimmy', 'Age': 25, 'Gender': 'Male', 'School': 'eMobillis'}
print(students['Name'])

print(f"Student Name: {students['Name']}")
print(f"Student Age: {students['Age']}")
print(f"Student Gender: {students['Gender']}")
print(f"Student School: {students['School']}")