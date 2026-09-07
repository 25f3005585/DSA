class Solution:
    def myPow(self, x: int, n: int, MOD) -> int:
        if n == 0:
            return 1

        if n == 1:
            return x

        call = self.myPow(x, (n // 2), MOD)
        if n & 1 == 0:
            return (call * call) % MOD
        else:
            return (x * call * call) % MOD

    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5

        MOD = (10**9) + 7
        ans = 1
        half = n // 2
        if (n & 1) == 0:
            odd = self.myPow(4, half, MOD)
            even = self.myPow(5, half, MOD)
            ans = odd * even
        else:
            odd = self.myPow(4, half, MOD)
            even = self.myPow(5, half + 1, MOD)
            ans = odd * even

        ans %= MOD
        return ans
