def bubble(input_array):
    l=len(input_array)
    for i in range(l):
        for j in range(l-i-1):
            if(input_array[j]>input_array[j+1]):
                temp=input_array[j]
                input_array[j]=input_array[j+1]
                input_array[j+1]=temp
    return input_array

arr=[2,0,7,5,3,9]
x=bubble(arr)
print(x)
