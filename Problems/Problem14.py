#There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

#Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
#Check
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        Brute Force 
        t=-1
        tval=-1
        n=len(gas)
        for i in range(len(gas)):
            #print("Round name", i)
            tanklevel=gas[i]
            for j in range(1,len(gas)):
                tanklevel-=cost[(i+j-1)%n]
                #print(tanklevel)
                if tanklevel>=0:
                    #print(cost[(i+j)%n])
                    t=1
                    #print(t,'t')
                else:
                    t=0
                    break
                tanklevel+=gas[(i+j)%n]
                #print((i+j)%n,'index')
                #print(tanklevel)
                if tanklevel>=cost[(i+j)%n]:
                    #print(cost[(i+j)%n])
                    t=1
                    #print(t,'t')
                else:
                    t=0
                    break
            if(t==1):
                tval=i
                break
            elif(t==-1 and len(gas)==1):
                if(gas[0]>=cost[0]):
                    tval=0
        '''
        #diff=[]
        tval=0
        difffinal=diff=0
        for i in range(len(gas)):
            difffinal+=gas[i]-cost[i]
        print(difffinal)
        for i in range(len(gas)):
            diff+=gas[i]-cost[i]
            if(diff<0):
                diff=0
                tval=(i+1)
        print(difffinal)
        """sum=0
        for i in range(len(gas)):
            sum+=diff[i]
        if(sum>=0):
            for i in range(len(gas)):
                if(diff[i]>0):
                    tval=i
                    break"""
        if(difffinal>=0):
            return tval
        else:
            return -1
        
        