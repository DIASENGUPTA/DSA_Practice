###RECHECK
#You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

#Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

#0 <= j <= nums[i] and
#i + j < n
#Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
class Solution:
    def jump(self, nums: List[int]) -> int:
        last=0
        ele=0
        jumps=0
        for i in range(len(nums)-1):
            ele=max(ele,i+nums[i])
            if(last==i):
                last=ele
                jumps+=1
        return jumps