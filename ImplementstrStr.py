class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0
        for i in range(len(haystack) - len(needle)+1):
            s = haystack[i:i + len(needle)]
            if s == needle:
                return i

        return -1


def main():
    print("Hello World!")
    solution = Solution()
    arg = 'abc'
    print(solution.strStr(arg, 'c'))


if __name__ == "__main__":
    main()
