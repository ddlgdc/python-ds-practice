def same_frequency(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)

    freq1 = {}
    freq2 = {}

    for digit in str_num1:
        freq1[digit] = freq1.get(digit, 0) + 1

    for digit in str_num2:
        freq2[digit] = freq2.get(digit, 0) + 1

    return freq1 == freq2