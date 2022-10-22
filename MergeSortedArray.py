from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # j = m
        # for i in range(n):
        #     nums1[j] = nums2[i]
        #     j = j + 1
        #
        # nums1.sort()
        # print(nums1)

        # while m > 0 and n > 0:
        #     if nums1[m - 1] >= nums2[n - 1]:
        #         nums1[m + n - 1] = nums1[m - 1]
        #         m -= 1
        #     else:
        #         nums1[m + n - 1] = nums2[n - 1]
        #         n -= 1
        #
        # if n > 0:
        #     nums1[:n] = nums2[:n]

        while  n > 0:
            if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n- 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        print(nums1)



# Driver program
if __name__ == '__main__':
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [2, 5, 6]
    m = 3
    n = 3
    solution = Solution()
    solution.merge(arr1, m, arr2, n)
    # print("result: ", result)
