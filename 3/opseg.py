class Opseg:
    def min(self, arr):
        ranges = 0
        previous = -1

        for i in arr:
            if previous != i - 1 and previous != -1:
                ranges += 1

            previous = i

        return ranges + 1
