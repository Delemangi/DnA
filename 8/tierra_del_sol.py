import collections


class TierraDelSol:
    def cena(self, N, M, X):
        self.prices = list(map(int, M.split(' ')))
        self.x = [list(map(int, row.split(' '))) for row in X]
        self.y = [[] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                self.y[j].append(self.x[j][i])

        visited = []
        prices = []
        taken_prices = []

        for i in range(N):
            if all(self.y[j][i] == 0 for j in range(N)):
                visited += self.dfs(i)
                prices.append(self.prices[i])
                taken_prices.append(i)

        not_visited = [i for i in range(N) if i not in visited]

        graph = Graph(len(not_visited))

        for i, a in enumerate(not_visited):
            for j, b in enumerate(not_visited):
                if self.y[a][b] == 1:
                    graph.add_edge(i, j)

        ssc = graph.ssc()

        for i in ssc:
            minimum, index = min((self.prices[not_visited[j]], not_visited[j]) for j in i)
            prices.append(minimum)
            taken_prices.append(index)

        not_taken_prices = [i for i in range(N) if i not in taken_prices]
        not_taken_prices.sort(key=lambda x: self.prices[x])

        for i in not_taken_prices:
            if self.prices[i] < sum(prices) // len(prices):
                prices.append(self.prices[i])
            else:
                break

        return sum(prices) // len(prices)

    def dfs(self, start):
        visited = []
        stack = collections.deque([start])

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(self.y[node])

        return visited


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
