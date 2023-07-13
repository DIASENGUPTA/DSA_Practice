#There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
class Solution:
    def candy(self, ratings: List[int]) -> int:
        output=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if(ratings[i-1]<ratings[i]):
                output[i]=output[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1] and output[i]<=output[i+1]:
                output[i]=output[i+1]+1
        print(output)
        return sum(output)