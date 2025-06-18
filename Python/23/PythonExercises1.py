def to_base13(num):
    if num == 0:
        return "0"

    digits = "0123456789ABC"
    is_negative = num < 0
    num = abs(num)
    
    result = []
    while num > 0:
        remainder = num % 13
        result.append(digits[remainder])
        num //= 13

    base13 = ''.join(reversed(result))
    return '-' + base13 if is_negative else base13
