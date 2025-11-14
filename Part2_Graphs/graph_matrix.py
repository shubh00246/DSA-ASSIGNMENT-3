class GraphMatrix:
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    def add_edge(self, u, v, w=1):
        """
        Undirected weighted graph using adjacency matrix.
        """
        self.matrix[u][v] = w
        self.matrix[v][u] = w

    def display(self):
        """
        Return adjacency matrix as list of rows.
        """
        return self.matrix


# Optional test when running this file alone
if __name__ == "__main__":
    g = GraphMatrix(5)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(3, 4, 6)

    print("Adjacency Matrix:")
    for row in g.display():
        print(row)
