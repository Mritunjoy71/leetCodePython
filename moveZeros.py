from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        shiftLen = len(nums)
        resultList = []
        count = 0
        # for i in range(shiftLen):
        #     if nums[i] == 0:
        #         count += 1
        #     else:
        #         resultList.append(nums[i])
        #
        # for i in range(count):
        #     resultList.append(0)
        #
        # for i in range(shiftLen):
        #     nums[i] = resultList[i]

        # insertPos = 0
        # for i in range(shiftLen):
        #     if nums[i] == 0:
        #         count += 1
        #     else:
        #         nums[insertPos] = nums[i]
        #         insertPos += 1
        #
        # for i in range(count):
        #     nums[insertPos] = 0
        #     insertPos += 1

        insertPos = 0

        for i in range(shiftLen):
            if nums[i] != 0:
                temp = nums[insertPos]
                nums[insertPos] = nums[i]
                nums[i] = temp
                insertPos += 1

        print(nums)


def main():
    print("Hello World!")
    solution = Solution()
    arg = [0, 0, 1]
    solution.moveZeroes(arg)


if __name__ == "__main__":
    main()
