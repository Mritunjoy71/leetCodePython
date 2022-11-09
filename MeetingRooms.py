from typing import List


class Solution:
    def meetingRoom(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        lastEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end
            else:
                return False

        return True


# Driver program
if __name__ == '__main__':
    intervals = [[1, 2], [1, 2], [1, 2]]
    solution = Solution()
    result = solution.meetingRoom(intervals)
    print("result: ", result)
