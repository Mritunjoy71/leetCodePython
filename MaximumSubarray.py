import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        maxSum = nums[0]
        maxSumSoFar = nums[0]
        for i in range(1, len(nums)):
            maxSum = nums[i] + (0 if maxSum < 0 else maxSum)
            maxSumSoFar = max(maxSum, maxSumSoFar)

        return maxSumSoFar


# Driver program
if __name__ == '__main__':
    array = [-2, -1]
    solution = Solution()
    result = solution.maxSubArray(array)
    print("result: ", result)
