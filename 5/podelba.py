class Podelba:
    def vrednosti(self, N, M):
        nodes = set()
        ratios = {}

        for i in N:
            a = i.split(' ')

            nodes.add(a[0])
            nodes.add(a[1])

            ratios[a[0], a[1]] = float(a[2])
            ratios[a[1], a[0]] = 1 / float(a[2])

        flag = True

        while flag:
            flag = False

            for i in nodes:
                for j in nodes:
                    for k in nodes:
                        if i == j or i == k or j == k:
                            continue

                        if (i, j) in ratios and (k, j) in ratios and (i, k) not in ratios:
                            ratios[i, k] = ratios[i, j] / ratios[k, j]
                            ratios[k, i] = 1 / ratios[i, k]
                            flag = True

        result = []

        for i in M:
            a, b = i.split(' ')

            if (a, b) in ratios:
                result.append('%g' % round(ratios[a, b], 1))
            elif (a, b) not in ratios and a == b and a in nodes:
                result.append(1)
            else:
                result.append(-1)

        return ' '.join(map(str, result))
