class SoobrakjajGradot:
    def idea(self, N, M):
        graph = [[False for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if (M[i][j] == 'Y' and M[j][i] == 'N') or (M[i][j] == 'N' and M[j][i] == 'Y'):
                    graph[i][j] = True

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    graph[i][j] |= graph[i][k] and graph[k][j]

        for i in range(N):
            if graph[i][i]:
                return 'NO'

        return 'YES'
