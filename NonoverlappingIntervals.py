from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        lastEnd = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end
            else:
                count += 1
                lastEnd = min(lastEnd, end)

        return count


# Driver program
if __name__ == '__main__':
    intervals = [[1, 2], [1, 2], [1, 2]]
    solution = Solution()
    result = solution.eraseOverlapIntervals(intervals)
    print("result: ", result)
