from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        strDigits = ''
        for i in digits:
            strDigits += str(i)

        resultNum = int(strDigits)
        resultNum += 1
        strDigits = str(resultNum)
        for i in strDigits:
            result.append(int(i))
        return result


def main():
    print("Hello World!")
    solution = Solution()
    arg = [1, 2, 3, 4, 5, 9]
    result = solution.plusOne(arg)
    print(result)


if __name__ == "__main__":
    main()
