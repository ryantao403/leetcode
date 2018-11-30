class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.optimal(nums, target)

    def brute_force(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
    
    def solve_by_sorting(self, nums, target):
        nums.sort()
        i = 0
        j = len(nums) - 1
        total = nums[i] + nums[j]
        while total != target:
            if total < target:
                i += 1
            else:
                j -= 1
            total = nums[i] + nums[j]
        return [i, j]

    def optimal(self, nums, target):
        lookup = dict()
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]
            else:
                lookup[num] = i
        return [-1, -1]