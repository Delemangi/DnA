class HromatskiBroj:
    def boi(self, N, M):
        self.M = [i for i in M]

        return self.color(N)

    def color(self, V):
        result = [-1] * V
        result[0] = 0

        available = [False] * V

        for u in range(1, V):
            for i, c in enumerate(self.M[u]):
                if result[i] != -1 and c == 'Y':
                    available[result[i]] = True

            cr = 0
            while cr < V:
                if (available[cr] is False):
                    break
                cr += 1

            result[u] = cr

            for i, c in enumerate(self.M[u]):
                if result[i] != -1 and c == 'Y':
                    available[result[i]] = False

        return len(set(result))
