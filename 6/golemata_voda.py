class Kajche:
    def voda(self, N, M, G, S, T):
        graph = Graph(N)

        for i in G:
            i, j, w = map(int, i.split(' '))
            graph.add_edge_undirected(i - 1, j - 1, w)

        a = graph.dijkstra(S - 1)[T - 1]

        return -1 if a > 10 ** 9 else a


class Graph:
    def __init__(self, num_vertices):
        self.infinity = float('inf')
        self.num_vertices = num_vertices
        self.matrix = [[0 if col == row else self.infinity
                        for col in range(num_vertices)]
                       for row in range(num_vertices)]

    def add_edge_undirected(self, fr, to, weight=1):
        self.matrix[fr][to] = weight
        self.matrix[to][fr] = weight

    def dijkstra(self, start, path=False):
        dijkstra = [self.infinity] * self.num_vertices
        dijkstra[start] = 1

        paths = [[] for _ in range(self.num_vertices)]
        paths[start] = [start]

        visited = [False] * self.num_vertices

        for _ in range(self.num_vertices):
            u = min((dijkstra[v], v) for v in range(
                self.num_vertices) if not visited[v])[1]
            visited[u] = True

            for v in range(self.num_vertices):
                if dijkstra[v] > dijkstra[u] * self.matrix[u][v] and (
                        not visited[v]):
                    dijkstra[v] = dijkstra[u] * self.matrix[u][v]

                    if path:
                        paths[v] = paths[u] + [v]

        return (dijkstra, paths) if path else dijkstra
