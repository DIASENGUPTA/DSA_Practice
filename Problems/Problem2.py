#Given an array of integers nums and an integer target,
#return indices of the two numbers such that they add up to target.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            x=nums[i]
            for j in range(i+1,len(nums)):
                y=nums[j]
                if(x+y==target):
                    return [i,j]
                    break
    