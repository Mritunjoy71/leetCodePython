from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


# Driver program
if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    solution = Solution()
    result = solution.canJump(nums)
    print("result: ", result)
