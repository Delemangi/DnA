class Palindrom:
    def min(self, S):
        return min(left(S), right(S))


def left(string):
    length = 0

    for i in range(len(string) - 1, 0, -1):
        if string[-i:] == string[-i:][::-1]:
            length = len(string[-i:])
            break

    return string + string[:-length][::-1]

def right(string):
    length = 0

    for i in range(len(string) - 1, 0, -1):
        if string[:i] == string[:i][::-1]:
            length = len(string[:i])
            break

    return string[length:][::-1] + string
