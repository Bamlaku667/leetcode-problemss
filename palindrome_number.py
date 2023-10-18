def isPalindrome(self, x: int) -> bool:
        if x< 0:
            return False

        divider = 1
        while x >= 10 * divider:
            divider *= 10
        while x:     
            right = x % 10
            left = x // divider
            if left != right: 
                return False
            else:
                x = x % divider # removing the first
                x = x // 10 # removing the last
                divider = divider // 100


        return True