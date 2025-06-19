def k_radius_average(nums, k):
    n = len(nums)
    window_size = 2 * k + 1
    result = [-1] * n

    if window_size > n:
        return result

    # soma inicial da primeira janela
    window_sum = sum(nums[:window_size])

    for i in range(k, n - k):
        avg = window_sum / window_size
        result[i] = round(avg, 2)
        if i + k + 1 < n:
            window_sum += nums[i + k + 1] - nums[i - k]

    return result
