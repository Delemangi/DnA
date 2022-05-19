class PrviMaj:
    def broj(self, A, B):
        substrings = []

        for i in range(len(B) - len(A) + 1):
            substrings.append(B[i:i + len(A)])

        return sum(diff(A, substring) for substring in substrings)


def diff(str1, str2):
    return sum(abs(int(i) - int(j)) for i, j in zip(str1, str2))
