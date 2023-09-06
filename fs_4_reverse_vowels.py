def reverse_vowels(s):
    vowels = set("aeiou")

    string = list(s)
    i = 0
    x = len(s) - 1

    while i < x:
        if string[i].lower() not in vowels:
            i += 1
        elif string[x].lower() not in vowels:
            x -= 1
        else:
            string[i], string[x] = string[x], string[i]
            i += 1
            x -= 1

    return "".join(string)