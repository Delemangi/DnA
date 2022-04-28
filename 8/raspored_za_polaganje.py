class RasporedZaPolaganje:
    def raspored(self, N, M, X):
        courses = [set() for _ in range(N)]

        for v in X:
            j, i = map(int, v.split(' '))
            courses[i - 1].add(j - 1)

        passed = set()
        order = []
        f = True

        while f:
            f = False

            for i in range(N):
                if i not in passed and len(courses[i] - passed) == 0:
                    passed.add(i)
                    order.append(str(i + 1))
                    f = True

                    break

        return ' '.join(order) if len(order) == N else 'NE'
