def sum_pairs(nums, goal):
    seen_numbers = set()

    for num in nums:
        complement = goal - num 

        if complement in seen_numbers:
            return (complement, num)
        
        seen_numbers.add(num)
    
    return ()