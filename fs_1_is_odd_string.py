def is_odd_string(word):
    def char_position(char):
        return ord(char.lower()) - 96
    sum_of_position = sum(char_position(char) for char in word)

    return sum_of_position % 2 == 1