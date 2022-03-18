class ZlatnaRipka:
    def result(self, N, a, b):
        score = []
        list_a = []
        list_b = []

        for i in range(N):
            list_a.append(a[i])
            list_b.append(b[i])

            score.append(self.solve(list_a, list_b))

        return " ".join(map(str, score))

    def solve(self, a, b):
        a.sort()
        b.sort(reverse=True)

        sums = [x + y for x, y in zip(a, b)]

        return max(sums)
