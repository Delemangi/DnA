class Doktorska:
    def premestuvanja(self, N, A, B):
        images = []

        for i in range(N // 2):
            images.append((A + i * B) % N)

        images.sort()
        steps = 0

        for i in range(len(images)):
            steps += abs(images[i] - (2 * i + 1))

        return str(steps)
