class GradskiVodovod:
    def poroshuvachka(self, N, K, m):
        pipes = [tuple(map(int, i.split(' '))) for i in m]
        groups = list(range(N))
        total = 0

        pipes.sort(key=lambda x: self.weight(x))

        for pipe in pipes:
            if groups[pipe[0]] == groups[pipe[1]]:
                continue

            union = min(groups[pipe[0]], groups[pipe[1]])

            for i in range(len(groups)):
                if groups[i] == pipe[0] or groups[i] == pipe[1]:
                    groups[i] = union

            total += self.weight(pipe)

        return total

    def weight(self, pipe):
        return pipe[2] * 7 + pipe[3]
