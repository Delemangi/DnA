vocals = 'aeiouy'


def num_vocals(word: str) -> int:
    counter = 0

    for char in word:
        if char in vocals:
            counter += 1

    return counter


class HeaviestWord:
    def heaviest(self, words):
        heaviest_word = words[0]
        most_vocals = num_vocals(words[0])

        for word in words:
            if num_vocals(word) > most_vocals or num_vocals(word) == most_vocals and word < heaviest_word:
                heaviest_word = word
                most_vocals = num_vocals(word)

        return heaviest_word
