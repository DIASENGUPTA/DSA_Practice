#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        start=1
        end=1
        arr=[1]*len(nums)
        for i in range(n):
            arr[i]*=start
            start*=nums[i]
            arr[-i-1]*=end
            end*= nums[-i-1]
        return arr