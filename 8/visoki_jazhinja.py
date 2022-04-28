class Zgradi:
    def run(self, N, S):
        odd = sum(len(lst.split(' ')) % 2 == 1 for lst in S)

        if odd == 0:
            return 1
        elif odd == 2:
            return 2
        else:
            return 0
