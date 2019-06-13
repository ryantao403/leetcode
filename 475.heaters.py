#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n, i, ans = len(heaters), 0, 0
        
        for house in houses:
            while i + 1 < n and heaters[i+1] < house:
                i += 1
            ans = max(ans, min([abs(h - house) for h in heaters[i:i+2]]))
        return ans
            

