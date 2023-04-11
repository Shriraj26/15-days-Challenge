"""
Do a Union Find Solution for this!!

"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        for i in range(n):
            graph[i] = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def isValidTree(root, graph, visited, prev):
            visited.add(root)
            for neighbor in graph[root]:
                if neighbor in visited:
                    if neighbor != prev:
                        return False
                    else:
                        continue
                else:
                    if not isValidTree(neighbor, graph, visited, root):
                        return False

            return True

        visited = set()
        ans = 0
        for node in range(n):
            if node not in visited:
                if not isValidTree(node, graph, visited, None):
                    return False
                ans += 1

        return True if ans == 1 else False
