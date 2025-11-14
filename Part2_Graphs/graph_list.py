class GraphList:
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.adj_list = {i: [] for i in range(num_nodes)}

    def add_edge(self, u, v, w=1):
        """
        Undirected weighted graph represented using adjacency list.
        """
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))

    def display(self):
        """
        Returns adjacency list dict.
        """
        return self.adj_list


# Optional demo
if __name__ == "__main__":
    g = GraphList(5)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(3, 4, 6)

    print("Adjacency List:")
    for node in g.display():
        print(node, "->", g.display()[node])
