class Solution:
    def __init__(self):
        self.graph = []
        self.visited = []

    def dfs(self, node, count, N):
        self.visited[node] = True
        count += 1

        if count == N:
            return True

        for neighbor in self.graph[node]:
            if not self.visited[neighbor]:
                if self.dfs(neighbor, count, N):
                    return True

        self.visited[node] = False
        return False

    def check(self, N, Edges):
        self.graph = [[] for _ in range(N)]
        for u, v in Edges:
            self.graph[u - 1].append(v - 1)
            self.graph[v - 1].append(u - 1)

        self.visited = [False] * N

        for i in range(N):
            if self.dfs(i, 0, N):
                return True

        return False

# Example usage
N = 5  # Number of nodes
M = 6  # Number of edges
Edges = [
    [1, 2],
    [1, 4],
    [2, 3],
    [3, 4],
    [4, 5],
    [2, 5]
]

solution = Solution()
result = solution.check(N, Edges)
print("Hamiltonian Path Found" if result else "No Hamiltonian Path Found")
