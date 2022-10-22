class Solution:
    # def countPrimes(self, n: int) -> int:
    #     if n <= 2:
    #         return 0
    #     isNonPrime = [False]*n
    #     count = 0
    #     for i in range(2, n):
    #         if not isNonPrime[i]:
    #             count += 1
    #             j = 2
    #             while i * j < n:
    #                 isNonPrime[i * j] = True
    #                 j += 1
    #
    #     return count

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
