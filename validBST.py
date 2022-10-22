# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = - math.inf

    # def validate(self, root: Optional[TreeNode], low: Optional[TreeNode], high: Optional[TreeNode]) -> bool:
    #     if root is None:
    #         return True
    #     if (low is not None and root.val <= low.val) or (high is not None and root.val >= high.val):
    #         return False
    #     return self.validate(root.right, root, high) and self.validate(root.left, low, root)

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     return self.validate(root, None, None)

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #     stack = [(root, -math.inf, math.inf)]
    #     while stack:
    #         root, lower, upper = stack.pop()
    #         if not root:
    #             continue
    #         if root.val <= lower or root.val >= upper:
    #             return False
    #         stack.append((root.right, root.val, upper))
    #         stack.append((root.left, lower, root.val))
    #     return True

    # dfs inorder traversal
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     def inorder(root):
    #         if not root:
    #             return True
    #         if not inorder(root.left):
    #             return False
    #         if root.val <= self.prev:
    #             return False
    #         self.prev = root.val
    #         return inorder(root.right)
    #
    #     return inorder(root)

    # dfs inorder iterative
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= self.prev:
                return False
            self.prev = root.val
            root = root.right
        return True


def LevelOrder(root, val):
    if root is None:
        root = TreeNode(val)
        return root
    if val is None:
        return root
    if val <= root.val:
        root.left = LevelOrder(root.left, val)
    else:
        root.right = LevelOrder(root.right, val)
    return root


def constructBst(arr, n):
    if n == 0:
        return None
    root = None

    for i in range(0, n):
        root = LevelOrder(root, arr[i])

    return root


# function to print the inorder traversal
def inorderTraversal(root):
    if root is None:
        return None

    inorderTraversal(root.left)
    print(root.val, " ")
    inorderTraversal(root.right)


# Driver program
if __name__ == '__main__':
    arr = [5, 4, 6, None, None, 3, 7]
    n = len(arr)

    root = constructBst(arr, n)

    solution = Solution()
    result = solution.isValidBST(root)
    print("result: ", result)
