class IpAddresses:
    def count(self, S, K):
        self.s = S
        self.k = K
        self.cache = {}

        return self.rec(0, K)

    def rec(self, i, remaining_dots):
        count = 0

        if (i, remaining_dots) in self.cache:
            return self.cache[i, remaining_dots]

        if remaining_dots == 0 and i != len(self.s):
            return 0

        if remaining_dots == 0 and i == len(self.s):
            return 1

        count += self.rec(i + 1, remaining_dots - 1)

        if i + 2 <= len(self.s) and self.s[i] != '0':
            count += self.rec(i + 2, remaining_dots - 1)

        if i + 3 <= len(self.s) and self.s[i] != '0' and int(self.s[i:i+3]) < 256:
            count += self.rec(i + 3, remaining_dots - 1)

        self.cache[i, remaining_dots] = count
        return count
