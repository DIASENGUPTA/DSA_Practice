#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small=0
        large=1
        prof=0
        for i in range(1,len(prices)):
            x=prices[i]-prices[small]
            if prices[small]<prices[i]:
                prof=max(prof,x)
            else:
                small=i
        return prof


##RECHECK
#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

#On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

#Find and return the maximum profit you can achieve.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        for i in range(1,len(prices)):
            if(prices[i]>prices[i-1]):
                prof+=prices[i]-prices[i-1]
        return prof