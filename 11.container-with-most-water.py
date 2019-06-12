#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            w = r - l
            if height[l] < height[r]:
                ans = max(ans, w * height[l])
                l += 1
            else:
                ans = max(ans, w * height[r])
                r -= 1
        return ans

