class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # Graph construction
        g = {i: [] for i in range(n)}
        for s, d, e in flights:
            g[s].append([d, e])

        def djikstra(source):

            visited = set()
            priQ = [(0, source)]
            dist = [float('inf')] * len(g)
            dist[source] = 0
            level = {source: 0}
            minCost = float('inf')
            while priQ:

                # process the current node
                _, currNode = heapq.heappop(priQ)

                # loop neighbors
                for dest, destWeight in g[currNode]:

                    # if not visited
                    if dest not in visited:
                        visited.add(dest)

                        level[dest] = level[currNode] + 1

                        # process in
                        if dist[dest] > dist[currNode] + destWeight:
                            dist[dest] = dist[currNode] + destWeight
                            # Almighty heapppp pushh!!
                            heapq.heappush(priQ, (dist[dest], dest))

                        if dest == dst:
                            print(level, level[dest])
                        # if we reached dest
                        if dest == dst and level[dest] <= k + 1:
                            print('Umm we are here ',
                                  level[dest], k, level[dest] <= k+1)
                            minCost = min(minCost, dist[dest])

                        visited.remove(dest)

            # print(dist)
            # print(minCost)
            return minCost

        minCost = djikstra(src)
        if minCost == float('inf'):
            return -1
        return minCost

        # return 0
