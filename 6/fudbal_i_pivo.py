class Fudbal:
    def pivo(self, L, D, M):
        graph = Graph(L)

        for i in M:
            i, j, w = map(int, i.split(' '))
            graph.add_edge_undirected(i - 1, j - 1, w)

        if max(graph.dijkstra(0)) > 10 ** 9:
            return -1

        a = [(max(graph.dijkstra(i)[:5]) - min(graph.dijkstra(i)[:5]), i) for i in range(5, L)]
        b = min(a)[0]
        best = 10 ** 9

        for s, i in a:
            if s == b:
                best = min(max(graph.dijkstra(i)[:]), best)

        return best


class Graph:
    def __init__(self, num_vertices):
        self.infinity = float('inf')
        self.num_vertices = num_vertices
        self.matrix = [[0 if col == row else self.infinity
                        for col in range(num_vertices)]
                       for row in range(num_vertices)]

    def add_edge_undirected(self, fr, to, weight=1):
        self.matrix[fr][to] = min(weight, self.matrix[fr][to])
        self.matrix[to][fr] = min(weight, self.matrix[to][fr])

    def dijkstra(self, start, path=False):
        dijkstra = [self.infinity] * self.num_vertices
        dijkstra[start] = 0

        paths = [[] for _ in range(self.num_vertices)]
        paths[start] = [start]

        visited = [False] * self.num_vertices

        for _ in range(self.num_vertices):
            u = min((dijkstra[v], v) for v in range(
                self.num_vertices) if not visited[v])[1]
            visited[u] = True

            for v in range(self.num_vertices):
                if dijkstra[v] > dijkstra[u] + self.matrix[u][v] and (
                        not visited[v]):
                    dijkstra[v] = dijkstra[u] + self.matrix[u][v]

                    if path:
                        paths[v] = paths[u] + [v]

        return (dijkstra, paths) if path else dijkstra
