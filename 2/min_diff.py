class MinDif:
    def minTransformations(self, N, S):
        capacity = sum(S) // 2
        dp = [0 for _ in range(capacity + 1)]

        for i in range(1, N + 1):
            for j in range(capacity, 0, -1):
                if S[i - 1] <= j:
                    dp[j] = max(dp[j], dp[j - S[i - 1]] + S[i - 1])

        return sum(S) - 2 * dp[capacity]
