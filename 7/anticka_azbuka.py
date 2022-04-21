class AntichkaAzbuka:
    def check(self, A):
        words = A.split(' ')
        alphabet = {}

        for word in words:
            for i, c1 in enumerate(word):
                for j, c2 in enumerate(word):
                    if i < j:
                        alphabet[c1, c2] = 1

                        if (c2, c1) in alphabet:
                            return 'Impossible'

        return 'Possible'
