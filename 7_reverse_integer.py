def reverse(x):
    MAX = 2**31 - 1
    MIN = -(2**31)

    if x > 0: 
        sign = 1
    else:
        sign = -1 
        x = -x

    output = 0
    while x > 0:
        last_digit = x % 10
        x = x // 10 # storing the remaining digit
        if output == (MAX //10) and last_digit >= MAX % 10:
            return 0
        if output > (MAX // 10):
            return 0
        output = output * 10 + last_digit
    return output * sign

