from queue import Queue


class SashoNaOdmor:
    def tezhina(self, N, M, x, s, t):
        edges = []

        for edge in x:
            i, j, w = map(int, edge.split(' '))
            edges.append((i - 1, j - 1, w - 1))
            edges.append((j - 1, i - 1, w - 1))

        weights = list(set(edge[2] for edge in edges))
        weights.sort()

        left = 0
        right = len(weights) - 1

        while left <= right:
            mid = (left + right) // 2
            weight = weights[mid]

            graph = Graph(N)

            for edge in edges:
                if edge[2] >= weight:
                    graph.add_edge_undirected(edge[0], edge[1], edge[2])

            if t - 1 in graph.connected_vertices(s - 1):
                left = mid + 1
            else:
                right = mid - 1

        return weights[left]


class Graph:
    def __init__(self, num_vertices):
        self.infinity = float('inf')
        self.num_vertices = num_vertices
        self.matrix = [[0 if col == row else self.infinity
                        for col in range(num_vertices)]
                       for row in range(num_vertices)]

    def add_edge_directed(self, fr, to, weight=1):
        self.matrix[fr][to] = weight

    def add_edge_undirected(self, fr, to, weight=1):
        self.matrix[fr][to] = weight
        self.matrix[to][fr] = weight

    def is_adjacent(self, fr, to):
        return self.matrix[fr][to] != self.infinity

    def connected_vertices(self, start):
        queue = Queue()
        queue.put(start)
        connected = {start}

        while not queue.empty():
            vertex = queue.get()

            for i in range(self.num_vertices):
                if self.matrix[vertex][i] < self.infinity and (
                        i not in connected):
                    connected.add(i)
                    queue.put(i)

        return connected

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

    def bellman_ford(self, start, path=False):
        bf = [self.infinity] * self.num_vertices
        bf[start] = 0

        paths = [[] for _ in range(self.num_vertices)]
        paths[start] = [start]

        for _ in range(self.num_vertices - 1):
            for u in range(self.num_vertices):
                for v in range(self.num_vertices):
                    if bf[u] + self.matrix[u][v] < bf[v]:
                        bf[v] = bf[u] + self.matrix[u][v]

                        if path:
                            paths[v] = paths[u] + [v]

        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if bf[u] + self.matrix[u][v] < bf[v]:
                    bf = False
                    paths = False

        return (bf, paths) if path else bf

    def floyd_warshall(self, path=False):
        fw = [[w for w in row] for row in self.matrix]
        paths = [[[i, j] if i != j else [i] for j in range(self.num_vertices)]
                 for i in range(self.num_vertices)]

        for m in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if fw[i][m] + fw[m][j] < fw[i][j]:
                        fw[i][j] = fw[i][m] + fw[m][j]

                        if path:
                            paths[i][j] = paths[i][m][:-1] + paths[m][j]

        return (fw, paths) if path else fw
