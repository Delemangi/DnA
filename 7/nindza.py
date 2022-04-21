import queue


class Ninja:
    def run(self, N, k, A, B):
        self.N = N
        self.k = k
        self.walls = {
            'A': A,
            'B': B
        }

        return 'yes' if self.bfs() else 'no'

    def bfs(self):
        q = queue.Queue()
        q.put((0, 'A', 0))
        q.put((0, 'B', 0))

        while not q.empty():
            height, wall, water = q.get()

            if height >= self.N:
                return True

            if self.walls[wall][height] == 'X' or height < water:
                continue

            q.put((height + 1, wall, water + 1))
            q.put((height - 1, wall, water + 1))

            if wall == 'A':
                q.put((height + self.k, 'B', water + 1))
            else:
                q.put((height + self.k, 'A', water + 1))

        return False
