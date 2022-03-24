class Gradina:
    def check(self, A, B):
        s = A + B

        return 'Y' if max(s.count(c) for c in s) <= len(s) // 2 else 'N'
