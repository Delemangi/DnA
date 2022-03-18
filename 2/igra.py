class Igra:
    def optimalChoice(self, cost):
        table = [list(map(int, row)) for row in cost]

        a, b = len(table), len(table[0])

        minimum = 2 ** 63

        for i in range(a):
            for j in range(b):
                maximum = 0

                dp = [[2 ** 63 for _ in range(b)] for _ in range(a)]
                dp[i][j] = table[i][j]

                for x in range(i, a):
                    for y in range(j, b):
                        if x == i and y == j:
                            continue

                        dp[x][y] = min(
                            dp[x - 1][y] if x - 1 >= 0 else 2 ** 63,
                            dp[x][y - 1] if y - 1 >= 0 else 2 ** 63
                        ) + table[x][y]

                        maximum = max(maximum, dp[x][y])

                for x in range(i, -1, -1):
                    for y in range(j, b):
                        if x == i and y == j:
                            continue

                        dp[x][y] = min(
                            dp[x + 1][y] if x + 1 < a else 2 ** 63,
                            dp[x][y - 1] if y - 1 >= 0 else 2 ** 63
                        ) + table[x][y]

                        maximum = max(maximum, dp[x][y])

                for x in range(i, a):
                    for y in range(j, -1, -1):
                        if x == i and y == j:
                            continue

                        dp[x][y] = min(
                            dp[x - 1][y] if x - 1 >= 0 else 2 ** 63,
                            dp[x][y + 1] if y + 1 < b else 2 ** 63
                        ) + table[x][y]

                        maximum = max(maximum, dp[x][y])

                for x in range(i, -1, -1):
                    for y in range(j, -1, -1):
                        if x == i and y == j:
                            continue

                        dp[x][y] = min(
                            dp[x + 1][y] if x + 1 < a else 2 ** 63,
                            dp[x][y + 1] if y + 1 < b else 2 ** 63
                        ) + table[x][y]

                        maximum = max(maximum, dp[x][y])

                # print(i, j)
                # print(dp)
                minimum = min(minimum, maximum)

        return minimum
