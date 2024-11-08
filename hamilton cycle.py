class Graph:
    def __init__(self):
        self.dict = {}

    def add_edge(self, u, v):
        if u not in self.dict:
            self.dict[u] = []

        if v not in self.dict:
            self.dict[v] = []

        self.dict[u].append(v)
        self.dict[v].append(u)

    def hamilton_cycle(self):
        # Helper function to check if the current vertex can be added to the path
        def is_valid_vertex(v, pos, path):
            # Check if this vertex is an adjacent vertex of the previously added vertex
            if v not in self.dict[path[pos - 1]]:
                return False

            # Check if the vertex has already been included
            if v in path:
                return False

            return True

        # Recursive utility function to solve the Hamiltonian Cycle problem
        def hamilton_cycle_util(path, pos):
            # Base case: If all vertices are included in the path
            if pos == len(self.dict):
                # Check if the last vertex is connected to the first vertex to form a cycle
                if path[0] in self.dict[path[pos - 1]]:
                    return True
                else:
                    return False

            # Try different vertices as the next candidate in the Hamiltonian Cycle
            for v in self.dict:
                if is_valid_vertex(v, pos, path):
                    path[pos] = v

                    if hamilton_cycle_util(path, pos + 1):
                        return True

                    # Backtrack
                    path[pos] = -1

            return False

        # Initializing the path and starting point
        path = [-1] * len(self.dict)
        starting_vertex = list(self.dict.keys())[0]
        path[0] = starting_vertex

        # Check if there is a Hamiltonian Cycle
        if not hamilton_cycle_util(path, 1):
            return "No Hamiltonian Cycle found."
        else:
            path.append(path[0])  # To show the cycle returning to the start
            return path

# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 1)
g.add_edge(2, 4)

print(g.hamilton_cycle())
