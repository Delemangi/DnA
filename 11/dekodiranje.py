class Dekodiranje:
    def poraka(self, M, S, k):
        indexes = []
        spaces = 0
        flag = True

        for i in range(len(M)):
            mistakes = 0
            spaces = 0

            for j in range(len(S)):
                if i + j + spaces >= len(M):
                    break

                if M[i + j + spaces] == ' ':
                    spaces += 1

                if i + j + spaces >= len(M):
                    break

                if M[i + j + spaces] != S[j]:
                    mistakes += 1

                if mistakes > k:
                    break
            else:
                if M[i] != ' ':
                    indexes.append(i)

                if mistakes > len(S) // 2:
                    flag = False

        return (' '.join(str(i) for i in indexes) + ('NO' if not indexes else ' YES' if flag else ' NO')).strip()
