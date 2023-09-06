def multiple_letter_count(phrase):
    counter = {}

    for letter in phrase:
        counter[letter] = counter.get(letter, 0) + 1
    return counter