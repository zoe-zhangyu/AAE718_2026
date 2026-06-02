#%%-1
def hello(input_1):
    return f"Hello {input_1}, my name is Zoë."

#%%-2
def divisible(x):
    return [i for i in range(10001) if i % x == 0]

#%%-3
def remove_none(d):
    return {key: value for key, value in d.items() if value is not None}

#%%-4
def length(L):
    count = 0
    for item in L:
        count += 1
    return count

#%%-5
def my_reverse(L):
    out = []
    for item in L:
        out = [item] + out
    return out

#%%-6
def my_min(L):
    current_min = L[0]
    for item in L:
        if item < current_min:
            current_min = item
    return current_min

#%%-7
def written_numbers(n):
    ones = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    def number_to_words(num):
        if num < 20:
            return ones[num]
        elif num < 100:
            ten_part = num // 10 * 10
            one_part = num % 10
            if one_part == 0:
                return tens[ten_part]
            else:
                return tens[ten_part] + " " + ones[one_part]
        else:
            hundred_part = num // 100
            rest = num % 100
            if rest == 0:
                return ones[hundred_part] + " hundred"
            else:
                return ones[hundred_part] + " hundred " + number_to_words(rest)

    return {i: number_to_words(i) for i in range(n + 1)}

#%%-8
def fizzbuzz(n):
    out = ""
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            out += "fizzbuzz\n"
        elif i % 3 == 0:
            out += "fizz\n"
        elif i % 5 == 0:
            out += "buzz\n"
    return out
