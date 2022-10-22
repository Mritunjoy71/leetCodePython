from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            dictionary = {}
            for i in range(9):
                if row[i] in dictionary:
                    return False
                elif row[i] != '.':
                    dictionary[row[i]] = True

        for i in range(9):
            dictionary = {}
            for j in range(9):
                if board[j][i] in dictionary:
                    return False
                elif board[j][i] != '.':
                    dictionary[board[j][i]] = True

        row = 0
        column = 0
        for i in range(9):
            dictionary = {}
            for j in range(row, row + 3):
                for k in range(column, column + 3):
                    if board[j][k] in dictionary:
                        return False
                    elif board[j][k] != '.':
                        dictionary[board[j][k]] = True

            if i == 2:
                row = j + 1
                column = 0
            elif i == 5:
                row = j + 1
                column = 0
            else:
                row = j - 2
                column = k + 1

        return True


def main():
    print("Hello World!")
    solution = Solution()
    arg = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(solution.isValidSudoku(arg))


if __name__ == "__main__":
    main()
