def flip_case(phrase, to_swap):
    result = ''

    for char in phrase:
        if char.lower() == to_swap.lower():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char 
        return result