from collections import defaultdict

class Graph:
    def __init__(self):
        self.dict = defaultdict(list)
        self.time = 0  # Time counter for DFS

    def add_edge(self, u, v):
        self.dict[u].append(v)
        self.dict[v].append(u)

    # Function to find and print biconnected components
    def biconnected_components(self):
        def dfs(u, parent):
            # nonlocal time
            visited[u] = True
            discovery[u] = low[u] = self.time
            self.time += 1
            children = 0

            for v in self.dict[u]:
                if not visited[v]:  # If v is not visited
                    parent_map[v] = u
                    children += 1
                    dfs(v, u)

                    # Check if the subtree rooted at v has a connection back to an ancestor of u
                    low[u] = min(low[u], low[v])

                    # Articulation point check
                    if parent_map[u] is None and children > 1:
                        articulation_points.add(u)
                    if parent_map[u] is not None and low[v] >= discovery[u]:
                        articulation_points.add(u)

                    # If u-v is a bridge
                    if low[v] > discovery[u]:
                        bridges.append((u, v))
                elif v != parent:
                    low[u] = min(low[u], discovery[v])

        visited = defaultdict(bool)
        discovery = defaultdict(lambda: float('inf'))
        low = defaultdict(lambda: float('inf'))
        parent_map = defaultdict(lambda: None)
        articulation_points = set()
        bridges = []

        for u in self.dict:
            if not visited[u]:
                dfs(u, None)

        print("Articulation Points:", articulation_points)
        print("Bridges:", bridges)

    # Function to find and print strongly connected components
    def strongly_connected_components(self):
        def dfs_scc(v):
            nonlocal scc_count
            discovery[v] = low[v] = self.time
            self.time += 1
            stack.append(v)
            in_stack[v] = True

            for neighbor in self.dict[v]:
                if discovery[neighbor] == -1:  # If neighbor is not visited
                    dfs_scc(neighbor)
                    low[v] = min(low[v], low[neighbor])
                elif in_stack[neighbor]:
                    low[v] = min(low[v], discovery[neighbor])

            # If v is the root of an SCC
            if low[v] == discovery[v]:
                scc = []
                while True:
                    node = stack.pop()
                    in_stack[node] = False
                    scc.append(node)
                    if node == v:
                        break
                sccs.append(scc)
                scc_count += 1

        discovery = defaultdict(lambda: -1)
        low = defaultdict(lambda: -1)
        in_stack = defaultdict(bool)
        stack = []
        sccs = []
        scc_count = 0

        for u in self.dict:
            if discovery[u] == -1:
                dfs_scc(u)

        print("Strongly Connected Components:", sccs)


# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 6)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

# Print Biconnected components (for undirected graph)
g.biconnected_components()

# For directed graph and SCCs, modify add_edge for directed connections
g_directed = Graph()
g_directed.add_edge(1, 2)
g_directed.add_edge(2, 3)
g_directed.add_edge(3, 1)
g_directed.add_edge(3, 4)
g_directed.add_edge(4, 5)
g_directed.add_edge(5, 4)

# Print Strongly Connected Components (for directed graph)
g_directed.strongly_connected_components()
