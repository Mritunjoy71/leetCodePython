class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictionary = {}
        for i in s:
            if i in dictionary:
                dictionary[i] = dictionary[i] + 1
            else:
                dictionary[i] = 1
        for i in range(len(s)):
            if dictionary[s[i]] == 1:
                return i

        return -1


def main():
    print("Hello World!")
    solution = Solution()
    arg = 'loveleetcode'
    print(solution.firstUniqChar(arg))


if __name__ == "__main__":
    main()
