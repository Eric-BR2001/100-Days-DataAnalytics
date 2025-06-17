def find_max_average(nums, k):
    max_sum = curr_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        curr_sum = curr_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, curr_sum)

    average = max_sum / k
    return round(average, 2)
