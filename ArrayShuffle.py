import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            swapIndex = random.randrange(i, len(self.array))
            temp = self.array[i]
            self.array[i] = self.array[swapIndex]
            self.array[swapIndex] = temp

        return self.array


# Driver program
if __name__ == '__main__':
    nums = [2, 3, 5, 9]
    obj = Solution(nums)
    # array = obj.reset()
    # print(array)
    array = obj.shuffle()
    print(array)
    array = obj.shuffle()
    print(array)
    array = obj.shuffle()
    print(array)
