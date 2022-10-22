from _ast import List


class Solution:
    def reverse(self, nums: List[int], i: int, j: int) -> None:
        while i < j:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == [] or len(nums) < 2:
            return
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
