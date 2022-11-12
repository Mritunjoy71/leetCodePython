from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroInFirstRow = False
        rowLen, colLen = len(matrix), len(matrix[0])
        for r in range(rowLen):
            for c in range(colLen):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        zeroInFirstRow = True

        for r in range(1, rowLen):
            for c in range(1, colLen):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(1, rowLen):
                matrix[r][0] = 0

        if zeroInFirstRow:
            for c in range(0, colLen):
                matrix[0][c] = 0

        print("result: ", matrix)


# Driver program
if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution = Solution()
    solution.setZeroes(matrix)
