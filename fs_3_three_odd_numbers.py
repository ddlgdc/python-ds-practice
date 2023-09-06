def three_odd_numbers(nums):
    for i in range(len(nums) - 2):
        subsequence = nums[i:i+3]

        if sum(subsequence) % 2 == 1:
            return True

    return False