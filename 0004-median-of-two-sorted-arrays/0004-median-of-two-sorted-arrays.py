class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = n1 + n2
        half = n // 2

        start = 0
        end = n1

        while start <= end:
            part1 = (start + end) // 2
            part2 = half - part1

            l1 = nums1[part1 - 1] if part1 > 0 else float('-inf')
            l2 = nums2[part2 - 1] if part2 > 0 else float('-inf')
            r1 = nums1[part1] if part1 < n1 else float('inf')
            r2 = nums2[part2] if part2 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return float(min(r1,r2))
                else:
                    a = min(r1,r2)
                    b = max(l1,l2)
                    return (a + b) / 2
            else:
                if l2 > r1:
                    start = part1 + 1
                elif l1 > r2:
                    end = part1 - 1
        return 0
