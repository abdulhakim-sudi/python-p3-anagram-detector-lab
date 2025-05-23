class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        sorted_word = sorted(self.word)
        result = []
        for candidate in candidates:
            if candidate.lower() != self.word and sorted(candidate.lower()) == sorted_word:
                result.append(candidate)
        return result  # <--- Make sure to return the result list
