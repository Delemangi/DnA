import queue


class ChovechkiResursi:
    def max(self, N, M, T, X, Y):
        graph = HashGraph(N + M + 2)
        s = N + M
        t = N + M + 1

        for edge in X:
            i, j = map(int, edge.split(' '))
            graph.add_edge(i, N + j, 1)
            graph.add_edge(s, i, 1)

        for edge in Y:
            i, j = map(int, edge.split(' '))
            graph.add_edge(N + i, t, j)

        return graph.ford_fulkerson(s, t)


class Graph:
    def __init__(self, num_vertices):
        self.inf = float('inf')
        self.num_vertices = num_vertices
        self.graph = None

    def add_edge(self, fr, to, weight=0):
        raise NotImplemented

    def weight(self, fr, to):
        raise NotImplemented

    def get_edges_list(self):
        raise NotImplemented

    def connected(self, src):
        connections_set = {src}
        q = queue.Queue()
        q.put(src)

        while not q.empty():
            vertex = q.get()

            for i in range(self.num_vertices):
                if self.weight(vertex, i) < self.inf and i not in connections_set:
                    connections_set.add(i)
                    q.put(i)

        return connections_set

    def dijkstra(self, src, path=False):
        D = [self.inf] * self.num_vertices
        D[src] = 0
        paths = [[] for _ in range(self.num_vertices)]
        paths[src] = [src]
        visited_vertices = [False] * self.num_vertices

        for _ in range(self.num_vertices):
            u = min((D[v], v) for v in range(self.num_vertices) if not visited_vertices[v])[1]
            visited_vertices[u] = True

            for v in range(self.num_vertices):
                if D[v] > D[u] + self.weight(u, v) and not visited_vertices[v]:
                    D[v] = D[u] + self.weight(u, v)

                    if path:
                        paths[v] = paths[u] + [v]

        return (D, paths) if path else D

    def bellman_ford(self, src, path=False):
        D = [self.inf] * self.num_vertices
        D[src] = 0
        paths = [[] for _ in range(self.num_vertices)]
        paths[src] = [src]

        for _ in range(self.num_vertices - 1):
            for u in range(self.num_vertices):
                for v in range(self.num_vertices):
                    if D[u] + self.weight(u, v) < D[v]:
                        D[v] = D[u] + self.weight(u, v)

                        if path:
                            paths[v] = paths[u] + [v]

        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if D[u] + self.weight(u, v) < D[v]:
                    D = False
                    paths = False

        return (D, paths) if path else D

    def kruskal_minimum_spanning_tree(self):
        result = []
        i = 0
        e = 0
        edges = sorted(self.get_edges_list(), key=lambda edge: edge[1])
        parent = []
        rank = []

        for node in range(self.num_vertices):
            parent.append(node)
            rank.append(0)

        while e < self.num_vertices - 1:
            (u, v), w = edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append(((u, v), w))
                self.union(parent, rank, x, y)
        return result

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def ford_fulkerson(self, src, dest):
        residual_graph = {}

        for (fr, to), weight in self.get_edges_list():
            if fr not in residual_graph:
                residual_graph[fr] = {}
            if to not in residual_graph[fr]:
                residual_graph[fr][to] = 0
            residual_graph[fr][to] += weight
            if to not in residual_graph:
                residual_graph[to] = {}
            if fr not in residual_graph[to]:
                residual_graph[to][fr] = 0

        maximum_capacity = 0

        while True:
            q = queue.Queue()
            parent_map = {}
            visited = set()
            q.put(src)
            visited.add(src)
            flag = True

            while not q.empty() and flag:
                current = q.get()

                for neighbour in residual_graph[current]:
                    if residual_graph[current][neighbour] > 0 and neighbour not in visited:
                        visited.add(neighbour)
                        q.put(neighbour)
                        parent_map[neighbour] = current

                        if neighbour == dest:
                            flag = False
                            break

            if flag:
                break

            minimum_capacity = self.inf
            current = dest

            while current != src:
                previous = parent_map[current]
                minimum_capacity = min(minimum_capacity, residual_graph[previous][current])
                current = previous

            maximum_capacity += minimum_capacity
            current = dest

            while current != src:
                previous = parent_map[current]
                residual_graph[previous][current] -= minimum_capacity
                residual_graph[current][previous] += minimum_capacity
                current = previous

        return maximum_capacity


class MatrixGraph(Graph):
    def __init__(self, num_vertices):
        super().__init__(num_vertices)
        self.graph = [[self.inf if column != row else 0 for column in range(num_vertices)]
                      for row in range(num_vertices)]

    def add_edge(self, fr, to, weight=0):
        self.graph[fr][to] = min(self.graph[fr][to], weight)

    def weight(self, fr, to):
        return self.graph[fr][to]

    def get_edges_list(self):
        edges = []
        for fr, row in enumerate(self.graph):
            for to, weight in enumerate(row):
                if weight != self.inf and fr != to:
                    edges.append(((fr, to), weight))
        return edges

    def floyd_warshall(self, path=False):
        D = [[w for w in row] for row in self.graph]
        paths = [[[i, j] if i != j else [i] for j in range(self.num_vertices)] for i in range(self.num_vertices)]

        for m in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if D[i][m] + D[m][j] < D[i][j]:
                        D[i][j] = D[i][m] + D[m][j]

                        if path:
                            paths[i][j] = paths[i][m][:-1] + paths[m][j]

        return (D, paths) if path else D


class HashGraph(Graph):
    def __init__(self, num_vertices):
        super().__init__(num_vertices)
        self.graph = {}

    def add_edge(self, fr, to, weight=0):
        if (fr, to) in self.graph:
            self.graph[fr, to] = min(self.graph[fr, to], weight)
        else:
            self.graph[fr, to] = weight

    def weight(self, fr, to):
        if (fr, to) in self.graph:
            return self.graph[fr, to]
        else:
            return self.inf

    def get_edges_list(self):
        return list(self.graph.items())
