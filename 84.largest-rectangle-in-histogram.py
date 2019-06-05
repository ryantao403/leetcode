#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_index, right_index = [n-1] * n, [0] * n

        stack = []
        for i in range(0, n, 1):
            h = heights[i]
            while stack and heights[stack[-1]] > h:
                left_index[stack.pop()] = i-1
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            h = heights[i]
            while stack and heights[stack[-1]] > h:
                right_index[stack.pop()] = i+1
            stack.append(i)

        ans = 0
        for i in range(n):
            h = heights[i]
            w = left_index[i] - right_index[i] + 1
            ans = max(ans, h*w)

        return ans