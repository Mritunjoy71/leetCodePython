class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        countT, countWindow = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        res, resLen = [-1, -1], float("infinity")
        need = len(countT)
        have = 0
        for right in range(len(s)):
            c = s[right]
            countWindow[c] = countWindow.get(c, 0) + 1
            if c in countT and countWindow[c] == countT[c]:
                have += 1
            while have == need:
                if resLen > (right - left + 1):  # update length
                    resLen = (right - left + 1)
                    res = [left, right]
                countWindow[s[left]] -= 1
                if s[left] in countT and countWindow[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        l, right = res
        return s[l: right + 1] if resLen != float("infinity") else ""


# Driver program
if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    print(solution.minWindow(s, t))
