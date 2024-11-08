class FloydWarshall:
    def __init__(self, vertices):
        self.V = vertices
        # Initialize the distance matrix with infinity and set diagonal elements to 0
        self.dist = [[float('inf')] * vertices for _ in range(vertices)]
        for i in range(vertices):
            self.dist[i][i] = 0

    def add_edge(self, u, v, weight):
        # Add an edge to the distance matrix
        self.dist[u][v] = weight

    def floyd_warshall(self):
        # Perform the Floyd-Warshall algorithm
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.dist[i][k] != float('inf') and self.dist[k][j] != float('inf') and \
                       self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
        return self.dist

# Example Usage
fw_graph = FloydWarshall(4)
fw_graph.add_edge(0, 1, 3)
fw_graph.add_edge(0, 2, 5)
fw_graph.add_edge(1, 2, 2)
fw_graph.add_edge(1, 3, -2)
fw_graph.add_edge(2, 3, 1)
fw_graph.add_edge(3, 0, 2)

result = fw_graph.floyd_warshall()
print("All pairs shortest paths:")
for row in result:
    print(row)
