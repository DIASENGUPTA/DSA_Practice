#You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.

#Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        flag=False
        last=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            #print(len(nums)-i)
            #print(nums[i])
            if(nums[i]>=(last-i)):
                last=i
                print("JHere")
                flag=True
            else:
                flag=False
        if(len(nums)==1):
            flag=True
        return flag
            