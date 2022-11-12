from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                topLeft = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft

            left += 1
            right -= 1

        print(matrix)


# Driver program
if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    solution.rotate(matrix)
