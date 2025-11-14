class Kruskal:
    def __init__(self, adj_list):
        """
        adj_list format:
        { node: [(neighbor, weight), ...] }
        """
        self.graph = adj_list
        self.nodes = list(adj_list.keys())

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    def minimum_spanning_tree(self):
        edges = []

        # convert adjacency list to edge list
        for u in self.graph:
            for v, w in self.graph[u]:
                edges.append((w, u, v))

        edges = list(set(edges))  # remove duplicates
        edges.sort()  # sort by weight

        parent = {node: node for node in self.nodes}
        rank = {node: 0 for node in self.nodes}

        mst = []

        for w, u, v in edges:
            if self.find(parent, u) != self.find(parent, v):
                self.union(parent, rank, u, v)
                mst.append((u, v, w))

        return mst


# Optional standalone demo
if __name__ == "__main__":
    sample_graph = {
        0: [(1, 4), (2, 2)],
        1: [(0, 4), (3, 5)],
        2: [(0, 2), (3, 8)],
        3: [(1, 5), (2, 8), (4, 6)],
        4: [(3, 6)]
    }

    k = Kruskal(sample_graph)
    print("Kruskal MST:")
    print(k.minimum_spanning_tree())
