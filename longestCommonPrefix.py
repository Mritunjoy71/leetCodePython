import math
from typing import List


class Solution:
    def commonPrefix(self, strs: List[str], minLen) -> bool:
        for i in range(minLen):
            ch = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != ch:
                    return False

        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        minLen = math.inf
        for s in strs:
            minLen = min(minLen, len(s))
        low = 1
        high = minLen
        while low <= high:
            mid = int((low + high) / 2)
            if self.commonPrefix(strs, mid):
                low += 1
            else:
                high = mid - 1

        return strs[0][:int((low + high) / 2)]


def main():
    print("Hello World!")
    solution = Solution()
    arg = ["flower", "flow", "flight"]
    print("Result: ", solution.longestCommonPrefix(arg))


if __name__ == "__main__":
    main()
