class Transform:
    def count(self, a, b):
        self.a = a
        self.b = b

        return self.shift()

    def shift(self):
        solution = -1

        for i in range(len(self.a)):
            m = self.diff(self.a[-i:] + self.a[:-i])

            if solution == -1 or solution > m + i:
                solution = m + i

        return solution

    def diff(self, list):
        return sum(abs(self.b[i] - list[i]) for i in range(len(list)))
