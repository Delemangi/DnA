import queue


class NapredenRasipanTelefon:
    def max_min(self, N, M, X):
        self.graph = [[] for _ in range(N)]
        self.words = [[] for _ in range(N)]
        self.N = N
        minimum = 2 ** 63
        maximum = 0

        for edge in X:
            i, j = map(int, edge.split(' '))
            self.graph[i - 1].append(j - 1)

        for v in range(N):
            self.bfs(v)

        for i in self.words:
            result = self.words.count(i)

            minimum = min(minimum, result)
            maximum = max(maximum, result)

        return '{} {}'.format(maximum, minimum)

    def bfs(self, start):
        q = queue.Queue()
        q.put(start)

        visited = [False for _ in range(self.N)]

        while not q.empty():
            i = q.get()

            if visited[i]:
                continue

            visited[i] = True
            self.words[i].append(start)

            for j in self.graph[i]:
                q.put(j)
