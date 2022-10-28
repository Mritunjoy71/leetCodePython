import collections
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest


# Driver program
if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    solution = Solution()
    result = solution.longestConsecutive(nums)
    print("result: ", result)
