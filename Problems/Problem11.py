#Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

#According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        t=0
        if(n>1):
            for i in range(n-1,-1,-1):
                if(citations[i]>=n-i):
                    t=n-i
        else:
            if(citations[0]==0):
                t=0
            else:
                t=1
        return t