from collections import defaultdict


class Graph:
    def __init__(self, edges=None):
        self.adj_list = defaultdict(list)

        if edges:
            for from_vertex, to_vertex in edges:
                self.add_edge(from_vertex, to_vertex)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.adj_list[from_vertex].append(to_vertex)

    def get_adjacency_list(self):
        return self.adj_list

    def print_graph(self):
        for row in self.adj_list:
            print(f"{row}->{self.adj_list[row]}")



edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "A")]
graph = Graph(edges=edges)

print("Список смежности:")
graph.print_graph()


graph.add_vertex("E")
graph.add_edge("D", "E")

print("\nОбновлённый список смежности:")
graph.print_graph()