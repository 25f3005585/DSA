class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        xor = 0
        for i in range(1, (n * n) + 1):
            xor ^= i

        for i in range(n):
            for j in range(n):
                xor ^= grid[i][j]

        bit_no = 0
        temp = xor

        while (temp & 1) == 0:
            temp >>= 1
            bit_no += 1

        zero = 0
        one = 0

        for i in range(n):
            for j in range(n):
                elem = grid[i][j]
                if ((elem >> bit_no) & 1) == 1:
                    one ^= grid[i][j]
                else:
                    zero ^= grid[i][j]

        for i in range(1, (n * n) + 1):
            elem = i
            if ((elem >> bit_no) & 1) == 1:
                one ^= i
            else:
                zero ^= i
        
        count = 0

        for row in grid:
            for num in row:
                if num == zero:
                    count += 1

        if count == 2:
            return [zero, one]

        return [one, zero]