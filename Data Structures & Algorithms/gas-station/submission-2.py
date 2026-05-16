class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_cost = 0
        total_gas = 0
        n = len(gas)
        for i in range(n):
            total_cost += cost[i]
            total_gas += gas[i]
        if total_cost > total_gas:
            return -1
        current = 0
        ans = 0
        for i in range(n):
            current += gas[i]-cost[i]
            if current < 0:
                current = 0
                ans = i+1
        return ans
        