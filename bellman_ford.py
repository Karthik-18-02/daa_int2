class BellmanFord:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, src):
        # Initialize distances with infinity and set the distance to the source node as 0
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Relax all edges V-1 times
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Check for negative-weight cycles
        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Graph contains a negative-weight cycle")
                return None

        return dist

# Example usage
bf_graph = BellmanFord(5)
bf_graph.add_edge(0, 1, -1)
bf_graph.add_edge(0, 2, 4)
bf_graph.add_edge(1, 2, 3)
bf_graph.add_edge(1, 3, 2)
bf_graph.add_edge(1, 4, 2)
bf_graph.add_edge(3, 2, 5)
bf_graph.add_edge(3, 1, 1)
bf_graph.add_edge(4, 3, -3)

result = bf_graph.bellman_ford(0)
if result:
    print("Shortest distances from source 0:", result)
