from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            anagrams[tuple(count)].append(s)

        return anagrams.values()


# Driver program
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(strs))
