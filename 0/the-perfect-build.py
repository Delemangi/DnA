class ThePerfectBuild:
    def getStrongness(self, heroType, gold, n, items):
        items_list = parse_items(items, heroType)
        dp = [0] * (gold + 1)

        for i in range(gold + 1):
            for j in range(n):
                if (items_list[j][0] <= i):
                    dp[i] = max(dp[i], dp[i - items_list[j][0]] +
                                items_list[j][1])

        return dp[gold]


def parse_items(items, hero_type):
    items_split = items.split(',')
    items_list = []

    for item in items_split:
        tokens = item.split(';')

        price = int(tokens[0])
        strength = int(tokens[1])
        agility = int(tokens[2])
        intelligence = int(tokens[3])
        value = 0

        if hero_type == 'strength':
            value = strength * 100 + agility * 10 + intelligence
        elif hero_type == 'agility':
            value = agility * 100 + intelligence * 10 + strength
        else:
            value = intelligence * 100 + strength * 10 + agility

        items_list.append((price, value))

    return items_list
