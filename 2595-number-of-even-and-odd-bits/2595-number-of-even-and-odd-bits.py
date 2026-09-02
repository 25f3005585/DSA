class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        i = 0
        while n != 0:
            if n & 1:
                if i & 1:
                    odd += 1
                else:
                    even += 1
            i += 1
            n = n >> 1

        return [even, odd]
