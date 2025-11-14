class BFS_DFS:
    def __init__(self, adj_list):
        """
        adj_list should be a dictionary:
        { node: [(neighbor, weight), ...] }
        """
        self.graph = adj_list

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        order = []

        while queue:
            node = queue.pop(0)
            order.append(node)

            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start):
        visited = set()
        order = []
        self._dfs_recursive(start, visited, order)
        return order

    def _dfs_recursive(self, node, visited, order):
        visited.add(node)
        order.append(node)

        for neighbor, _ in self.graph[node]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, order)


# Optional demonstration
if __name__ == "__main__":
    sample_graph = {
        0: [(1, 4), (2, 2)],
        1: [(0, 4), (3, 5)],
        2: [(0, 2), (3, 8)],
        3: [(1, 5), (2, 8), (4, 6)],
        4: [(3, 6)]
    }

    obj = BFS_DFS(sample_graph)

    print("BFS from 0:", obj.bfs(0))
    print("DFS from 0:", obj.dfs(0))
