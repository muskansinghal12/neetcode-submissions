from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #next smallest to the left
        #next smallest to the right
        n = len(heights)
        left = []
        stack = deque()
        right = []
        ans = 0
        for i in range(0,n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                left.append(-1)
                # stack.append(i)
            else:
                left.append(stack[-1])
            stack.append(i)
        
        stack = deque()
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                right.insert(0,n)
                # stack.append(i)
            else:
                right.insert(0,stack[-1])
            stack.append(i)
        print(left)
        print(right)
        for i in range(n):
            ans = max((right[i]-left[i]-1)*heights[i], ans)
        return ans


        
