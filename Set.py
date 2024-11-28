# Sets are a collection type that stores unique, unordered, and mutable elements

# Note :
    # Sets are mutable but the elements are immutable
    
collection = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10}

print(type(collection))
print(collection)


# Methods in sets

collection.add(11) 
collection.add("ZGOD") 
print(collection)

collection.remove(5)
print(collection)



print(collection.pop()) # Pop the random element from the set 
print(collection.pop())
print(collection.pop())


# Union method

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
print(union_set) # Duplicate elements are ignored

# Intersection method

intersection_set = set1.intersection(set2)
print(intersection_set) # Gives the Common elements 