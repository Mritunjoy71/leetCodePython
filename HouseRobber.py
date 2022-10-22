import math
from typing import List


class Solution:
    def __init__(self):
        self.memory = {}

    # def rob(self, nums: List[int]) -> int:
    #     return self.robHelper(nums, len(nums) - 1)
    #
    # def robHelper(self, nums: List[int], i: int) -> int:
    #     if i < 0:
    #         return 0
    #     return max(self.robHelper(nums, i - 2) + nums[i], self.robHelper(nums, i - 1))

    # def rob(self, nums: List[int]) -> int:
    #     return self.robHelper(nums, len(nums) - 1)
    #
    # def robHelper(self, nums: List[int], i: int) -> int:
    #     if i < 0:
    #         return 0
    #     if i in self.memory:
    #         return self.memory[i]
    #     self.memory[i] = max(self.robHelper(nums, i - 2) + nums[i], self.robHelper(nums, i - 1))
    #     return self.memory[i]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        dp = {0: nums[0], 1: max(nums[0], nums[1])}
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]


# Driver program
if __name__ == '__main__':
    array = [2, 1, 1, 2]
    solution = Solution()
    result = solution.rob(array)
    print("result: ", result)
