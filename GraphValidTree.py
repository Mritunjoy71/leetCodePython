from typing import List


class Solution:
    def validGraphTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return
            visit.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)


# Driver program
if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    solution = Solution()
    result = solution.validGraphTree(n, edges)
    print("result: ", result)
