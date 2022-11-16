from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxFreq = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])
            while r - l + 1 - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


# Driver program
if __name__ == '__main__':
    s = "AABABBA"
    k = 1
    solution = Solution()
    print(solution.characterReplacement(s, k))
