class Prezentacii:
    def maxPrezentacii(self, N, sf):
        presentations = []
        count = 0
        time = 0

        for i in range(N):
            presentations.append((sf[2 * i], sf[2 * i + 1]))

        presentations.sort(key=lambda x: x[1])

        for x, y in presentations:
            if x < time:
                continue

            time = y
            count += 1

        return count
