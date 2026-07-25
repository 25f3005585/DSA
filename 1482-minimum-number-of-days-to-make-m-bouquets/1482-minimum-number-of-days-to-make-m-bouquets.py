class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        answer = -1
        start = min(bloomDay)
        end = max(bloomDay)

        while start <= end:
            mid = (start + end) // 2
            m_bouquets = 0
            k_flower = 0

            for bloom in bloomDay:
                if bloom <= mid:
                    k_flower += 1
                else:
                    k_flower = 0

                if k_flower == k:
                    m_bouquets += 1
                    k_flower = 0

            if m_bouquets >= m:
                end = mid - 1
                answer = mid
            else:
                start = mid + 1

        return answer
