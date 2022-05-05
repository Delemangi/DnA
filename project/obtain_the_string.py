def main():
    s = input()
    t = input()

    dp = [[2 ** 63 for _ in range(26)] for _ in range(len(s) + 1)]

    for i in range(len(s) - 1, -1, -1):
        for j in range(26):
            dp[i][j] = dp[i + 1][j]
        dp[i][ord(s[i]) - ord('a')] = i

    res = 1
    pos = 0

    for i in range(len(t)):
        if pos == len(s):
            pos = 0
            res += 1

        if dp[pos][ord(t[i]) - ord('a')] == 2 ** 63:
            pos = 0
            res += 1

        if dp[pos][ord(t[i]) - ord('a')] == 2 ** 63 and pos == 0:
            return -1

        pos = dp[pos][ord(t[i]) - ord('a')] + 1

    return res


if __name__ == '__main__':
    print(main())
