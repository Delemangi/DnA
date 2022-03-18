class Slatkara:
    def calculate(self, n, z):
        permutations = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3),
                        (1, 3, 9)]

        if n != 3:
            z += [0] * (3 - n)

        dp = [[[2 ** 63 for _ in range(z[2] + 1)] for _ in range(z[1] + 1)]
              for _ in range(z[0] + 1)]
        dp[0][0][0] = 0

        for i in range(z[0] + 1):
            for j in range(z[1] + 1):
                for k in range(z[2] + 1):
                    if i == j == k == 0:
                        continue

                    for a, b, c in permutations:
                        dp[i][j][k] = min(
                            dp[i][j][k],
                            dp[max(i - a, 0)][max(j - b, 0)][max(k - c, 0)] + 1
                        )

        return dp[z[0]][z[1]][z[2]]
