# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version >= 1:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        firstBadIndex = n
        low = 1
        high = n
        while low <= high:
            mid = int((low + high) / 2)
            isBad = isBadVersion(mid)
            if isBad:
                firstBadIndex = mid
                high = mid - 1
            else:
                low = mid + 1

        return firstBadIndex


# Driver program
if __name__ == '__main__':
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [2, 5, 6]
    m = 3
    n = 3
    solution = Solution()
    result = solution.firstBadVersion(3)
    print("result: ", result)
