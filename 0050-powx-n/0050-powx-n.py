class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        sign = n >= 0
        if sign:
            call = self.myPow(x, (n//2))
            if n & 1 == 0:
                return call * call
            else:
                return x * call * call
        else:
            x = 1 / x
            n = abs(n)
            call = self.myPow(x, (n//2))
            if n & 1 == 0:
                return call * call
            else:
                return x * call * call