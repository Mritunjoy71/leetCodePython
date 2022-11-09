from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        s, e = 0, 0
        count, maxCount = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            maxCount = max(maxCount, count)

        return maxCount


# Driver program
if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    solution = Solution()
    result = solution.minMeetingRooms(intervals)
    print("result: ", result)
