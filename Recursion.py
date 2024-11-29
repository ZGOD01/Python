# Recursion is basically when a function call itself repeatedly.

def show(n):
    if(n == 0): # Base Case (decide that the recursion should continue or not)
        return
    print(n)
    show(n-1)
    
show(5)