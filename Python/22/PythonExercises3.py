def two_sum_less_than_k(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1
    max_sum = -1

    while left < right:
        s = nums[left] + nums[right]
        if s < k:
            max_sum = max(max_sum, s)
            left += 1
        else:
            right -= 1

    return max_sum