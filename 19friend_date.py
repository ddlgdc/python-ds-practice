def friend_date(a, b):
    hobbies_a = set(a[2])
    hobbies_b = set(b[2])

    if hobbies_a.intersection(hobbies_b):
        return True
    else:
        return False