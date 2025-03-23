import heapq


# @leet start
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        dist = [float("inf")] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]

        MOD = 10**9 + 7

        # Dijkstra's algorithm
        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for neighbor, time in graph[node]:
                if dist[node] + time < dist[neighbor]:
                    dist[neighbor] = dist[node] + time
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (dist[neighbor], neighbor))
                elif dist[node] + time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]


# @leet end

