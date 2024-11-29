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

        color_map = {}

        for i in self.dict:

            color_set = set()

            for j in self.dict[i]:
                if j in color_map:
                    color_set.add(color_map[j])
                
            color = 1
            while color in color_set:
                color += 1

            if color > max_colors:
                return "impossible"
            
            color_map[i] = color

        return color_map

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

