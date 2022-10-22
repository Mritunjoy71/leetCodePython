class Solution:
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     one_step_before = 2
    #     two_step_before = 1
    #     totalStepCombination = 0
    #     for i in range(3, n + 1):
    #         totalStepCombination = one_step_before + two_step_before
    #         two_step_before = one_step_before
    #         one_step_before = totalStepCombination
    #
    #     return totalStepCombination

    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        steps = [1, 2]
        for i in range(1, n + 1):
            count = 0
            for j in steps:
                if i - j >= 0:
                    count += dp[i - j]
            dp[i] = count

        return dp[n]


# Driver program
if __name__ == '__main__':
    solution = Solution()
    result = solution.climbStairs(3)
    print("result: ", result)
