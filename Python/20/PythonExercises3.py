def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    if n == 1000:
        return "one thousand"
    elif n >= 100:
        rem = n % 100
        hundreds = ones[n // 100] + " hundred"
        if rem == 0:
            return hundreds
        else:
            return hundreds + " and " + number_to_words(rem)
    elif n >= 20:
        return tens[n // 10] + ("-" + ones[n % 10] if n % 10 != 0 else "")
    elif n >= 10:
        return teens[n - 10]
    else:
        return ones[n]

def count_letters_up_to_n(n):
    total = 0
    for i in range(1, n + 1):
        words = number_to_words(i)
        letters = words.replace(" ", "").replace("-", "")
        total += len(letters)
    return total
