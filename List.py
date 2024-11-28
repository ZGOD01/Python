# List can store multiple different values in a single  variable

RollNo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(RollNo)
print(type(RollNo))

# Note : 
    # Lists are mutable (can be changed)
    # Lists can contain different data types (integers, floats, strings)
    # Lists are ordered (elements can be accessed by their index)
    # Lists can be nested (lists can contain other lists)
    # Lists can have duplicate values
    
# Accessing elements of a list

print(RollNo[0]) # Accessing the first element
print(RollNo[4]) # Accessing the fifth element
print(RollNo[-1]) # Accessing the last element
print(RollNo[-5]) # Accessing the fifth last element

# Slicing a list (starting index : ending index) 

print(RollNo[2:5]) # Accessing elements from index 2 to 4 (not including 5)
print(RollNo[:5]) # Accessing elements from index 0 to 4 (not including 5)
print(RollNo[2:]) # Accessing elements from index 2 to the end
print(RollNo[:]) # Accessing all elements

# Modifying elements of a list

RollNo[2] = 100 # Changing the third element to 100
print(RollNo)

# List Methods : There are many methods available for lists, but I have included only the most frequently used ones.

list = [2, 1, 3 ] 

list.append(4)
print(list)

list.sort() # Default to ascending order
print(list)

list.reverse() # Reverse the whole list
print(list)

list.insert(1, 5) # Insert an element at a specific index (index , element)
print(list)

number = [0, 2, 4, 1, 2, 4, 1, 2,]
number.remove(2) # Remove first occurrence of element 
print(number)


marks = [99 , 75, 100, 101, 102,]
marks.pop(0) # Remove element at a specific index
print(marks)