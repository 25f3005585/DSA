class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)        
        i = 0

        while i < n and s[i] == " ":
            i+=1

        if i > n - 1:
            return 0

        is_negative = False
        left_range = -2 ** 31
        right_range = (2 ** 31) - 1
        
        if s[i] == "-":
            is_negative = True
            i+=1
        elif s[i] == "+":
            i+=1

        result = 0

        while i < n:
            ch = s[i]
            ch_number = ord(ch)

            if 48 <= ch_number <= 57:
                number = ch_number - 48
                result = result * 10 + number
            else:
                break
            i+=1

        result = -result if is_negative else result

        if result > right_range:
            return right_range
        elif result < left_range:
            return left_range
        else:
            return result

