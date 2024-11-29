class Solution:
    
    def bellman(self, V, adj, S):

        short_dist = V * [float('inf')]
        short_dist[S] = 0

        for _ in range(V-1):
            for i in adj:
                u, v, wt = i
                if short_dist[u] + wt < short_dist[v] and short_dist[u] != float('inf'):
                    short_dist[v] = short_dist[u] + wt

        for i in adj:
            u, v, wt = i
            if short_dist[u] + wt < short_dist[v] and short_dist[u] != float('inf'):
                return [-1]
            
        return short_dist
                

V = 5
edges = [
    [0, 1, -1],  # Edge from vertex 0 to 1 with weight -1
    [0, 2, 4],   # Edge from vertex 0 to 2 with weight 4
    [1, 2, 3],   # Edge from vertex 1 to 2 with weight 3
    [1, 3, 2],   # Edge from vertex 1 to 3 with weight 2
    [1, 4, 2],   # Edge from vertex 1 to 4 with weight 2
    [3, 2, 5],   # Edge from vertex 3 to 2 with weight 5
    [3, 1, 1],   # Edge from vertex 3 to 1 with weight 1
    [4, 3, -3]   # Edge from vertex 4 to 3 with weight -3
]
S = 0

solution = Solution()
print(solution.bellman(V, edges, S))