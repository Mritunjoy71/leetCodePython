# Definition for a binary tree node.
import math
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []
    #     answer = []
    #     queue = [root]
    #     while queue:
    #         temp = []
    #         for i in range(len(queue)):
    #             node = queue.pop(0)
    #             temp.append(node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #
    #         answer.append(temp)
    #
    #     return answer

    def helperLevelOrder(self, root: Optional[TreeNode], answer: List[List[int]], height: int) -> None:
        if not root:
            return
        if height >= len(answer):
            answer.append([])
        answer[height].append(root.val)
        self.helperLevelOrder(root.left, answer, height + 1)
        self.helperLevelOrder(root.right, answer, height + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        answer = []
        self.helperLevelOrder(root, answer, 0)

        return answer


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
    result = solution.levelOrder(root)
    print("result: ", result)
