"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    start=0
    end=len(input_array)
    l=len(input_array)
    c=0
    while(l>0):
        if(l%2==0):
            mid=(start+end)//2-1
        else:
            mid=(start+end)//2
        if(value>input_array[mid]):
            start=mid+1
        elif(value<input_array[mid]):
            end=mid-1
        elif(value==input_array[mid]):
            c=1
            return mid
        l=l//2
    if(c==0):
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
#binary_search(test_list, test_val1)
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))