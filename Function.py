# A function in Python is a block of reusable code that performs a specific task.

# Define a function
# def func_name(parameter1 , parameter2) : 
    # return output or print statement
    
def sum(a, b) : 
    print( a + b)

sum(2,3)

def avg(a, b, c) :
    print ((a + b + c) / 3)

avg(2, 3, 4)

# Function Types
    # 1) Built-in functions --> print() , len() , type() , range() 
    # 2) User-defined functions


    
 
def check_odd_even(): # user-defined function
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

check_odd_even()