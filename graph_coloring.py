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


    def graph_coloring(self, max_colors):
        # Result dictionary to store the color assigned to each vertex
        color_result = {}

        # Iterate over all vertices to assign colors
        for vertex in self.dict:
            # Create a set of all colors assigned to adjacent vertices
            adjacent_colors = set()
            for neighbor in self.dict[vertex]:
                if neighbor in color_result:
                    adjacent_colors.add(color_result[neighbor])

            # Find the first available color not used by adjacent vertices within the limit of max_colors
            color = 1
            while color in adjacent_colors:
                color += 1

            # Check if the color exceeds the allowed number of colors
            if color > max_colors:
                return "Graph cannot be colored with the given number of colors."

            # Assign the chosen color to the current vertex
            color_result[vertex] = color

        return color_result

# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 6)
g.add_edge(2, 3)
g.add_edge(3, 7)
g.add_edge(2, 4)
g.add_edge(7, 5)
g.add_edge(4, 5)

# Specify the maximum number of colors allowed
max_colors = 3
print(g.graph_coloring(max_colors))
print(g.add_edge())
