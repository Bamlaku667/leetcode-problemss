def myAtoi(s: str) -> int:
        MAX = 2**31 -1
        MIN = -2**31
        s = s.lstrip()
        if not s: 
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]

        elif s[0] == '+':
            sign = 1
            s = s[1:]
        output = 0
        for char in s:
            if char.isdigit():
                output = output * 10 + int(char)
            else: 
                break
        output = output * sign
        if output > MAX:
            output = MAX
        elif output < MIN:
            output = MIN

        return output

