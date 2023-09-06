def mode(nums):
    num_counts = {}

    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    most_common = max(num_counts, key=num_counts.get)
    return most_common