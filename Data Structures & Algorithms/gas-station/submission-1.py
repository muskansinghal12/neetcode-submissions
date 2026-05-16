class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(0,n):
            #starting
            if cost[i] <= gas[i]:
                start = i
                current = 0
                broke = False
                for j in range(i,n):
                    current += gas[j]-cost[j]
                    if current < 0:
                        broke = True
                        break
                if broke:
                    continue
                for j in range(0,i):
                    current += gas[j]-cost[j]
                    if current < 0:
                        broke = True
                        break
                if not broke:
                    return i
        return -1
                
                    
        