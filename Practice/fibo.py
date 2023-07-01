"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""
output=0
def get_fib(position):
    global output
    if position==0 or position==1:
        return position
    else:
        output= get_fib(position-1)+get_fib(position-2)
        return output
        
# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
