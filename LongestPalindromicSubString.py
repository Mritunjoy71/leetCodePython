class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        maxLen = 0
        result = ""

        for i in range(length):
            j, k = i, i
            while j >= 0 and k < length and s[j] == s[k]:
                j -= 1
                k += 1
            if k - j + 1 > maxLen:
                maxLen = k - j + 1
                result = s[j + 1: k]

            j, k = i, i + 1
            while j >= 0 and k < length and s[j] == s[k]:
                j -= 1
                k += 1
            if k - j + 1 > maxLen:
                maxLen = k - j + 1
                result = s[j + 1: k]

        return result


# Driver program
if __name__ == '__main__':
    s = "cbbd"
    solution = Solution()
    print(solution.longestPalindrome(s))
