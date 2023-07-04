#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times.
#  You may assume that the majority element always exists in the array.
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictnew=defaultdict()
        for i in nums:
            if i in dictnew.keys():
                dictnew[i]+=1
            else:
                dictnew[i]=1
            if(dictnew[i]>len(nums)/2):
                return i
                break

