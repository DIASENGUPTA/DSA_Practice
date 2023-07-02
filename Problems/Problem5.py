#Given an integer array nums sorted in non-decreasing order, 
# remove some duplicates in-place such that each unique element appears at most twice.
#  The relative order of the elements should be kept the same.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L=len(nums)
        i=0
        while i<L-2:
            if(nums[i]==nums[i+1]==nums[i+2]):
                nums.remove(nums[i])
                L-=1
                i-=1
            i+=1
        return len(nums)