from typing import List


class Solution:
    def encode(self, s: List[str]) -> str:
        result = ""
        for i in s:
            result += str(len(i)) + "#" + i
        return result

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        firstHash = True
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result


# Driver program
if __name__ == '__main__':
    inputList = ["lint", "code", "love", "you"]
    solution = Solution()
    res = solution.encode(inputList)
    print(solution.decode(res))
