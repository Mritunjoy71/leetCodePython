class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for i in range(2, n + 1):
            result = self.helper(result)
        return result

    def helper(self, s: str) -> str:
        result = ""
        i = 0
        while i < len(s):
            digit = s[i]
            i = i + 1
            count = 1
            while i < len(s) and digit == s[i]:
                count += 1
                i += 1
            result += str(count) + digit
        return result


# Driver program
if __name__ == '__main__':
    solution = Solution()
    result = solution.countAndSay(5)
    print("result: ", result)
