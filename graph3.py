class Graph:
    def __init__(self, vertices=None, edges=None):

        self.vertex_index = {}
        self.index_vertex = []
        self.matrix = []

        if vertices:
            for vertex in vertices:
                self.add_vertex(vertex)

        if edges:
            for from_vertex, to_vertex in edges:
                self.add_edge(from_vertex, to_vertex)

    def add_vertex(self, vertex):

        if vertex not in self.vertex_index:
            self.vertex_index[vertex] = len(self.index_vertex)
            self.index_vertex.append(vertex)


            for row in self.matrix:
                row.append(0)

            new_row = [0] * len(self.index_vertex)
            self.matrix.append(new_row)

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.vertex_index:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertex_index:
            self.add_vertex(to_vertex)

        from_idx = self.vertex_index[from_vertex]
        to_idx = self.vertex_index[to_vertex]
        self.matrix[from_idx][to_idx] = 1

    def get_adjacency_matrix(self):
        return self.matrix

    def print_graph(self):
        for row in self.matrix:
            print(row)


edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "A")]
graph = Graph(edges=edges)

print("Матрица смежности:")
graph.print_graph()


graph.add_vertex("E")
graph.add_edge("D", "E")

print("\nОбновлённая матрица смежности:")
graph.print_graph()