class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex, rib):
        self.graph[vertex].append(rib)

    def print_graph(self):
        for node in self.graph:
            print(f"{node}->{self.graph[node]}")



graph = Graph()


graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")





graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "A")
graph.add_edge("A", "E")
graph.add_edge("B", "E")
graph.add_edge("D", "E")



graph.print_graph()
