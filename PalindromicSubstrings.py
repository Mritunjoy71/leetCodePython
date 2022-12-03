class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        result = 0

        for i in range(length):
            j, k = i, i
            while j >= 0 and k < length and s[j] == s[k]:
                j -= 1
                k += 1
                result += 1

            j, k = i, i + 1
            while j >= 0 and k < length and s[j] == s[k]:
                j -= 1
                k += 1
                result += 1

        return result


# Driver program
if __name__ == '__main__':
    s = "aaa"
    solution = Solution()
    print(solution.countSubstrings(s))
