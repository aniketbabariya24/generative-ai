# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

def addData(dictionary, name, age):
    dictionary[name] = age

def updateAge(dictionary, name, newAge):
    if name in dictionary:
        dictionary[name] = newAge

def deleteAge(dictionary, name):
    if name in dictionary:
        del dictionary[name]

data = {}

addData(data, "John", 25)
print(data)  

updateAge(data, "John", 26)
print(data) 

deleteAge(data, "John")
print(data) 
