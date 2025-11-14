import heapq

class Dijkstra:
    def __init__(self, adj_list):
        """
        adj_list format:
        { node: [(neighbor, weight), ...] }
        """
        self.graph = adj_list

    def shortest_path(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        pq = [(0, start)]  # (distance, node)

        while pq:
            current_dist, node = heapq.heappop(pq)

            if current_dist > distances[node]:
                continue

            for neighbor, weight in self.graph[node]:
                new_dist = current_dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances


# Optional demo when executed alone
if __name__ == "__main__":
    sample_graph = {
        0: [(1, 4), (2, 2)],
        1: [(0, 4), (3, 5)],
        2: [(0, 2), (3, 8)],
        3: [(1, 5), (2, 8), (4, 6)],
        4: [(3, 6)]
    }

    d = Dijkstra(sample_graph)
    print("Dijkstra Shortest Paths from 0:")
    print(d.shortest_path(0))
