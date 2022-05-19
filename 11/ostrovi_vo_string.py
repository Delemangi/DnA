import collections


class Ostrovi:
    def stringovi(self, S, K):
        substrings = set()

        for i in range(len(S)):
            for j in range(i, len(S)):
                substrings.add(S[i:j + 1])

        islands = [count_islands(create_islands(S, substring, 'x' * len(substring))) for substring in substrings]
        counter = collections.Counter(islands)

        return counter[K]


def create_islands(string, substring, replace):
    m = [c for c in string]
    rep = [c for c in replace]

    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            m[i:i + len(substring)] = rep

    return ''.join(m)


def count_islands(string):
    counter = 0

    for i in range(1, len(string)):
        if string[i - 1] == 'x' and string[i] != 'x':
            counter += 1

    if string[-1] == 'x':
        counter += 1

    return counter
