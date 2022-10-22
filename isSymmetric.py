# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def checkSymmetric(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    #     if root1 is None and root2 is None:
    #         return True
    #     elif not root1 or not root2:
    #         return False
    #     elif root1.val != root2.val:
    #         return False
    #     else:
    #         return self.checkSymmetric(root1.left, root2.right) and self.checkSymmetric(root1.right, root2.left)

    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #     return self.checkSymmetric(root.left, root.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = []
        queue.append((root.left, root.right))
        while queue:
            root1, root2 = queue.pop(0)
            if root1 is None and root2 is None:
                continue
            elif not root1 or not root2:
                return False
            elif root1.val != root2.val:
                return False

            queue.append((root1.left, root2.right))
            queue.append((root1.right, root2.left))

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
    arr = [1, 2, 2, 3, 4, 4, 3]
    n = len(arr)

    root = constructBst(arr, n)

    solution = Solution()
    result = solution.isSymmetric(root)
    print("result: ", result)
