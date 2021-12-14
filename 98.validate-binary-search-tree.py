#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        return self.dfs(root, -float('inf'), float('inf'))  

    def dfs(self, root, low, high):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self.dfs(root.left, low, root.val) and self.dfs(root.right, root.val, high)
        
# @lc code=end

