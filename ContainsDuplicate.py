from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        diction = {}
        for i in nums:
            if not diction.get(i):
                diction[i] = 1
            else:
                diction[i] = diction[i] + 1

        for i in diction.keys():
            if diction.get(i) > 1:
                return True

        return False
