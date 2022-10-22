class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isNonPrime = [False] * n
        count = 0
        for i in range(2, n):
            if not isNonPrime[i]:
                j = i * i
                while j < n:
                    isNonPrime[j] = True
                    j += i
        for i in range(2, n):
            if not isNonPrime[i]:
                count += 1
        return count


# Driver program
if __name__ == '__main__':
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [2, 5, 6]
    m = 3
    n = 3
    solution = Solution()
    result = solution.firstBadVersion(3)
    print("result: ", result)
