class Graph:
    """Uses Adjacency List to keep track of vertices and edges"""
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def add_vertex(self, vertex) -> bool:
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2) -> bool:
        """Connect `v1` and `v2` bidirectionally"""
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:  # If the vertices exist but there are no edges between them
                pass

    def remove_vertex(self, vertex) -> bool:
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False



if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_vertex('A')
    my_graph.add_vertex('B')
    my_graph.add_vertex('C')
    my_graph.add_vertex('D')
    my_graph.add_edge('A', 'B')
    my_graph.add_edge('A', 'C')
    my_graph.add_edge('A', 'D')
    my_graph.add_edge('B', 'D')
    my_graph.add_edge('C', 'D')
    my_graph.print_graph()
    my_graph.remove_vertex('D')
    my_graph.print_graph()