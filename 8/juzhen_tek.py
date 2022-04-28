import collections


counter = 0


class JuzhenTek:
    def gradovi(self, N, S):
        global counter
        graph = Graph(len(S))

        for i, v in enumerate(S):
            for j in v.split(' '):
                graph.add_edge(i, int(j) - 1)

        return graph.ap()


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = collections.defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def ap_util(self, u, visited, ap, parent, low, disc):
        children = 0
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if visited[v] is False:
                parent[v] = u
                children += 1
                self.ap_util(v, visited, ap, parent, low, disc)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def ap(self):
        counter = 0

        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V)

        for i in range(self.V):
            if visited[i] is False:
                self.ap_util(i, visited, ap, parent, low, disc)

        for value in ap:
            if value is True:
                counter += 1

        return counter
