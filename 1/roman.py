class Roman:
    def countPages(self, N, K, arr):
        self.arr = arr
        self.n = N
        self.k = K

        return self.search()

    def search(self):
        left = 0
        right = sum(self.arr)

        while right >= left:
            middle = (left + right) // 2

            first_check = self.check(middle)
            second_check = self.check(middle + 1)

            if first_check and second_check:
                right = middle - 1
            elif not first_check and not second_check:
                left = middle + 1
            else:
                return middle + 1

    def check(self, max):
        total = 0
        heads = 1

        for i in range(self.n):
            if total + self.arr[i] > max:
                total = self.arr[i]
                heads += 1
            else:
                total += self.arr[i]

            if heads > self.k or total > max:
                return False

        return True
