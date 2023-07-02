#Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once.
#  The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L=len(nums)
        i=0
        while i<L-1:
            if(nums[i]==nums[i+1]):
                nums.remove(nums[i])
                L-=1
                i-=1
            i+=1
        return len(nums)



