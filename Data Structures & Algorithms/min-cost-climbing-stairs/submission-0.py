class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        
        sum_cost = [100*100+1]*(len(cost) + 1)
        sum_cost[0] = 0
        sum_cost[1] = 0
        for i in range(2, len(cost)+1):
            one_step_value = sum_cost[i-1] + cost[i-1]
            two_step_value = sum_cost[i-2] + cost[i-2]
            sum_cost[i] = min(one_step_value, two_step_value)
        return sum_cost[-1]



        