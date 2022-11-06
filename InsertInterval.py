from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        for interval in intervals:
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif interval[1] < newInterval[0]:
                result.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
            i += 1
        result.append(newInterval)
        return result


# Driver program
if __name__ == '__main__':
    intervals = []
    newInterval = [4, 8]
    solution = Solution()
    result = solution.insert(intervals, newInterval)
    print("result: ", result)
