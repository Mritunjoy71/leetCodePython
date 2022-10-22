# Definition for a binary tree node.
import math
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def helperToBST(self, nums: List[int], low: int, high: int) -> Optional[TreeNode]:
    #
    #     if low > high:
    #         return None
    #     mid = int((low + high) / 2)
    #     node = TreeNode(nums[mid])
    #     node.left = self.helperToBST(nums, low, mid - 1)
    #     node.right = self.helperToBST(nums, mid + 1, high)
    #     return node

    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    #     if len(nums) == 0:
    #         return None
    #     return self.helperToBST(nums, 0, len(nums) - 1)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = int(len(nums) / 2)
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST([nums[i] for i in range(0, mid)])
        node.right = self.sortedArrayToBST([nums[i] for i in range(mid + 1, len(nums))])
        return node


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
    arr = [-10, -3, 0, 5, 9]
    n = len(arr)

    root = constructBst(arr, n)

    solution = Solution()
    result = solution.sortedArrayToBST(arr)
    print("result: ", result)
