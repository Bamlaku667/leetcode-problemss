def isValid( s: str) -> bool:
        matches = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        opens_stack = []
        for char in s:
            if char in matches:
                opens_stack.append(char)
            else:
                if len(opens_stack) > 0 and matches[opens_stack[-1]] == char:
                    opens_stack.pop()
                else:
                    return False

        if len(opens_stack) > 0:
            return False
        else:
            return True

        
        