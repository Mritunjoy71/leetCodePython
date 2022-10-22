from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        print('transposed', matrix)
        return matrix

    def reflect(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)

        for i in range(n):
            for j in range(int(n / 2)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = temp

        print('reflected', matrix)
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print('Input Matrix: ', matrix)
        matrix = self.transpose(matrix)
        matrix = self.reflect(matrix)
        print('Result Matrix: ', matrix)


def main():
    print("Hello World!")
    solution = Solution()
    arg = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(arg)


if __name__ == "__main__":
    main()
