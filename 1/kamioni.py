class Kamioni:
    def min(self, items):
        items_list = [item for item in items if item < 200]
        counter = len(items) - len(items_list)
        items_list.sort()

        left = 0
        right = len(items_list) - 1

        while left < right:
            counter += 1

            if items_list[left] + items_list[right] <= 300:
                left += 1

            right -= 1

        if left == right:
            counter += 1

        return counter
