# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxSum = -float('inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            maxLeft = max(dfs(root.left), 0)
            maxRight = max(dfs(root.right), 0)
            self.maxSum = max((maxLeft + maxRight + root.val), self.maxSum)

            return root.val + max(maxLeft, maxRight)

        dfs(root)
        return self.maxSum
