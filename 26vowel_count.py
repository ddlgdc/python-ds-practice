def vowel_count(phrase):
    vowel_count = {}

    vowels = set('aeiouAEIOU')

    for char in phrase:
        if char.lower() in vowels:
            vowel_count[char.lower()] = vowel_count.get(char.lower(), 0) + 1
        return vowel_count 