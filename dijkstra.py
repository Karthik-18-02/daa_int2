import heapq
from typing import List

class Solution:
    def dijkstra(self, V: int, adj: List[List[List[int]]], S: int) -> List[int]:
        # min-heap priority queue
        pq = []
        heapq.heappush(pq, (0, S))

        short_dis = [float('inf')] * V
        short_dis[S] = 0

        while pq:

            dis, node = heapq.heappop(pq)

            for i in adj[node]:

                adjNode, edgeWt = i[0], i[1]

                if dis + edgeWt < short_dis[adjNode]:
                    short_dis[adjNode] = dis + edgeWt
                    heapq.heappush(pq, (short_dis[adjNode], adjNode))
        
        return short_dis


# Example usage:
# Number of vertices (V), adjacency list (adj), and source vertex (S)
V = 6
adj = [
    [[1, 4], [2, 4]],  # Adjacency list for vertex 0
    [[0, 4], [2, 2]],           # Adjacency list for vertex 1
    [[0, 4], [1, 2], [3, 3], [5, 6], [4, 1]],           # Adjacency list for vertex 2
    [[2, 3], [5, 2]],           # Adjacency list for vertex 3
    [[2, 1], [5, 3]],
    [[3, 2], [2, 6], [4, 3]],
]
S = 0

solution = Solution()
print(solution.dijkstra(V, adj, S))
