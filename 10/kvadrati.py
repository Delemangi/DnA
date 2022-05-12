class Kvadrati:
    def min(self, O):
        self.cache = {}
        i, j = map(int, O.split(' X '))

        return self.min_squares(i, j)

    def min_squares(self, m, n):
        if m == n:
            return 1

        if (m, n) in self.cache:
            return self.cache[m, n]

        min_ver = min([self.min_squares(m, i) + self.min_squares(m, n - i) for i in range(1, n // 2 + 1)], default=100000)
        min_hor = min([self.min_squares(i, n) + self.min_squares(m - i, n) for i in range(1, m // 2 + 1)], default=100000)
        result = min(min_hor, min_ver)
        self.cache[m, n] = result

        return result
