def sum_range(nums, start=0, end=None):
    if end is None or end > len(nums):
        end = len(nums)

    total = sum(nums[start:end])

    return total