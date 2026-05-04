class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        # ans = [0]*(n+1)
        # print(ans)
        first = 1
        second = 1
        for i in range(2,n+1):
            temp = first + second
            first = second
            second = temp
        # print(ans)
        return second
        