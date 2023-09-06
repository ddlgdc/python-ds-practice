def truncate(phrase, n):
    if n < 3:
        return 'Truncation mustbe at least 3 characters.'
    if len(phrase) <= n:
        return phrase
    
    truncated_phrase = phrase[:n - 3] + '...'

    return truncated_phrase