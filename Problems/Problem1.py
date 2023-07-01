#We are given two sorted arrays nums1 and nums2 of sizes m and n, respectively. 
# We need to merge these two arrays into a single sorted array, and the result should be stored inside nums1. 
# Since nums1 is of size m+n, we can use this extra space to store the merged array. 
# We can iterate through the arrays from the end and place the larger element in the end of nums1.

#Quick Sort Approach
class Solution:
    def partition(self,arr,low,high):
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if(arr[j]<pivot):
                i=i+1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
    def mergesort(self,arr,low,high):
        if low<high:
            pi=self.partition(arr,low,high)
            self.mergesort(arr,low,pi-1)
            self.mergesort(arr,pi+1,high)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,m+n):
            nums1[i]=nums2[i-m]
        self.mergesort(nums1,0,m+n-1)
        print(nums1)

#Normal Apprach
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,m+n):
            nums1[i]=nums2[i-m]
        nums1.sort()
        print(nums1)