from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 1, len(height) - 2
        maxLeft, maxRight = height[0], height[len(height) - 1]
        maxWater = 0
        while left <= right:
            if maxLeft < maxRight:
                maxWater += (maxLeft - height[left]) if (maxLeft - height[left]) > 0 else 0.
                maxLeft = max(maxLeft, height[left])
                left += 1
            else:
                maxWater += (maxRight - height[right]) if (maxRight - height[right]) > 0 else 0.
                maxRight = max(maxRight, height[right])
                right -= 1

        return int(maxWater)


# Driver program
if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution = Solution()
    print(solution.trap(height))
