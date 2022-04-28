import collections


class GrupiNaDoverba:
    def run(self, P, T, A):
        graph = Graph(P)

        for v in A:
            i, j = map(int, v.split(' '))
            graph.add_edge(i - 1, j - 1)

        a = graph.ssc()

        return '{} {} {}'.format(len(a), len(min(a, key=len)), len(max(a, key=len)))


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = collections.defaultdict(list)
        self.ssc_list = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True

        self.ssc_list.append(v)

        for i in self.graph[v]:
            if visited[i] is False:
                self.dfs_util(i, visited)

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] is False:
                self.fill_order(i, visited, stack)
        stack = stack.append(v)

    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def ssc(self):
        sscs = []

        stack = []
        visited = [False] * (self.V)

        for i in range(self.V):
            if visited[i] is False:
                self.fill_order(i, visited, stack)

        gr = self.transpose()

        visited = [False] * (self.V)

        while stack:
            i = stack.pop()
            if visited[i] is False:
                gr.dfs_util(i, visited)
                sscs.append(gr.ssc_list[:])
                gr.ssc_list = []

        return sscs
