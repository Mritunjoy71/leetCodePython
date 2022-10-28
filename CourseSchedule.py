from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisitesMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prerequisitesMap[crs].append(pre)
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if prerequisitesMap[crs] is []:
                return True
            visitSet.add(crs)
            for pre in prerequisitesMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            prerequisitesMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


# Driver program
if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print("result: ", result)
