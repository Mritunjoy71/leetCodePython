class Solution:

    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
        # ss = list(s)
        # copyS = list(s)
        n = len(s)
        # for i in range(int(n / 2)):
        #     ss[i], ss[n - i - 1] = ss[n - i - 1], ss[i]
        #
        # return copyS == ss

        for i in range(int(n / 2)):
            if s[i] != s[n - i - 1]:
                return False
        return True


def main():
    print("Hello World!")
    solution = Solution()
    arg = 'A man, a plan, a canal: Panama'
    print(solution.isPalindrome(arg))


if __name__ == "__main__":
    main()
