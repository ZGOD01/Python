# Dictionaries in python are key value pairs

dict = {
    "name" : "ZGOD",
    "age" : 23,
    "city" : "New York"
}
print(dict)


# Accessing values using keys
print(dict["name"]) # Output: ZGOD
print(dict["age"]) # Output: 23


# Adding a new key-value pair
dict["gender"] = "Male"
print(dict) # Output: {'name': 'ZGOD', 'age': 23, 'city': 'New York', 'gender': 'Male'}


# Updating a value
dict["age"] = 24
print(dict) # Output: {'name': 'ZGOD', 'age': 24, 'city': 'New York', 'gender': 'Male'}


# Removing a key-value pair
del dict["city"]
print(dict) # Output: {'name': 'ZGOD', 'age': 24, 'gender': 'Male'}

# Nested dictionary 

info = {
    "name" : "ZGOD",
    "age" : 23,
    "address" : {
        "street" : "123 Main St",
        "city" : "New York"
    }
}

# Dictionary Methods : There are many methods available for dictionary, but I have included only the most frequently used ones .

print(list(info.keys())) # Return the keys 

print(list(info.values())) # Return the values

print(list(info.items()))  # Return the (key , value) pairs as tuple

print(info.get("name")) # Return the value according to key

info.update({"dept": "AI & DS"})
print(list(info.items()))

