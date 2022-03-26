class Let:
    def cena(self, costs, minDays):
        graph = []
        cost = 0

        for i in costs:
            graph.append(list(map(int, i.replace('-', str(2 ** 63)))))

        for _ in range(int(minDays)):
            cost += min(min(i) for i in graph)

        print(cost)
