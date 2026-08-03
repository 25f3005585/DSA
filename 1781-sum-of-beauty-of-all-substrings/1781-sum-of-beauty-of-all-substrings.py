class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total_sum = 0

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                index = ord(s[j]) - 97
                freq[index] += 1

                minimum = float("inf")
                maximum = 0

                for k in range(26):
                    if freq[k] > 0:
                        minimum = min(minimum,freq[k])
                        maximum = max(maximum,freq[k])
                total_sum += (maximum - minimum)

        return total_sum
