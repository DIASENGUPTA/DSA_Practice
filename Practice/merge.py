def merge(input_array):
    if(len(input_array)>1):
        mid=len(input_array)//2
        L=input_array[:mid]
        R=input_array[mid:]
        merge(L)
        merge(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if(L[i]<=R[j]):
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            k+=1
            i+=1
        while j<len(R):
            arr[k]=R[j]
            k+=1
            j+=1
    return arr


arr=[0,1,2,1,3,10,8]
arr1=merge(arr)
print(arr1)
