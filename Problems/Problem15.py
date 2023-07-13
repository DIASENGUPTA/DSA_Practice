#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
class Solution:
    def romanToInt(self, s: str) -> int:
        romandict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=1
        num=romandict[s[0]]
        #print(romandict[s[2]])
        while i<len(s):
            if s[i] in ['V','X']:
                if s[i-1]=='I':
                    num+=-2*romandict[s[i-1]]
            if s[i] in ['L','C']:
                if s[i-1]=='X':
                    num+=-2*romandict[s[i-1]]
            if s[i] in ['D','M']:
                if s[i-1]=='C':
                    num+=-2*romandict[s[i-1]]
            num+=romandict[s[i]]
            i+=1
        return num