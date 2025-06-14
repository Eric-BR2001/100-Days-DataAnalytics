def plus_one(digits):
    n = len(digits)
    
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits  # done, no carry needed
        digits[i] = 0  # carry over to next digit

    # if loop completes, all digits were 9
    return [1] + digits
