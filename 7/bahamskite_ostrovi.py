import queue


class BahamskiOstrovi:
    def ostorvi(self, N, M, X):
        self.X = [list(map(int, i.split(' '))) for i in X]
        self.N = N
        self.M = M
        self.visited = [[False for _ in range(self.M)] for _ in range(self.N)]

        c = 0

        for i in range(self.N):
            for j in range(self.M):
                if self.X[i][j] == 1 and self.visited[i][j] is False:
                    self.bfs(i, j)
                    c += 1

        return c

    def bfs(self, i, j):
        q = queue.Queue()
        q.put((j, i))

        while not q.empty():
            x, y = q.get()

            if x < 0 or y < 0 or x >= self.M or y >= self.N or self.visited[y][x] is True or self.X[y][x] == 0:
                continue

            self.visited[y][x] = True

            q.put((x - 1, y))
            q.put((x + 1, y))
            q.put((x, y - 1))
            q.put((x, y + 1))

            q.put((x - 1, y - 1))
            q.put((x - 1, y + 1))
            q.put((x + 1, y - 1))
            q.put((x + 1, y + 1))
