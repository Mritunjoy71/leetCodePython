from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        dictionary1 = {}
        dictionary2 = {}
        for i in range(len(nums1)):
            if str(nums1[i]) in dictionary1:
                dictionary1[str(nums1[i])] = dictionary1[str(nums1[i])] + 1
            else:
                dictionary1[str(nums1[i])] = 1

        for j in range(len(nums2)):
            if str(nums2[j]) in dictionary2:
                dictionary2[str(nums2[j])] = dictionary2[str(nums2[j])] + 1
            else:
                dictionary2[str(nums2[j])] = 1

        for key in dictionary1.keys():
            print(key)
            if key in dictionary2:
                print('dictionary1[key] ' + str(dictionary1[key]))
                print('dictionary2[key] ' + str(dictionary2[key]))
                n = min(dictionary1[key], dictionary2[key])
                print('n ' + str(n))
                for k in range(0, n):
                    result.append(int(key))

        return result
