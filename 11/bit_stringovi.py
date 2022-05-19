import re

class BitStringovi:
    def broj(self, A, B):
        substrings = set()
        counter = 0

        for i in range(len(A) - len(B) + 1):
            substrings.add(A[i:i + len(B)])

        for substring in substrings:
            if re.fullmatch(B.replace('?', '.'), substring):
                counter += 1

        return counter
