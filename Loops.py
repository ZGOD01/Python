# While Loop 

count = 1
while count <= 5 :
    print(count)
    count += 1
print("Loop Ended!")
    
# Using (break) in loop

num = 1
while num <=5 :
    if num == 3:
        break
    print(num)
    num += 1
print("Loop Ended!")

    
# Using (continue) in loop

sum = 1
while sum <=5 :
    if(sum == 3) :
        sum += 1
        continue
    print(sum)
    sum += 1
print("Loop Ended!")


# For Loop 

nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in nums :
    print(val)
    
    
# For Loop with using else 
   
for val in nums :
    if val == 5 :
        print("Found 5")
        break
    print(val)
else :
    print("5 not found")
    
    
# range() function in for loop

for i in range(10) : #range(ending index)
    print(i)
print("Loop Ended!")


for i in range(2, 10) : # range(starting index , ending index)
    print(i)
print("Loop Ended!")

for i in range(1, 10 , 2) : # range(starting index , ending index , steps(means increment by..?))
    print(i)
print("Loop Ended!")
