from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex, rib):
        self.graph[vertex].append(rib)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque()
        result = []

        if start_vertex not in self.graph:
            return result

        queue.append(start_vertex)
        visited.add(start_vertex)

        while queue:
            current_vertex = queue.popleft()
            result.append(current_vertex)

            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

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


print("Граф:")
print(graph)

start_vertex = "A"
bfs_result = graph.bfs(start_vertex)
print(f"\nBFS обход начиная с вершины '{start_vertex}': {bfs_result}")

graph.print_graph()
