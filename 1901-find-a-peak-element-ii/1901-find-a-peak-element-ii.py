class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        start = 0
        end = n - 1

        while start <= end:
            mid = (start + end) // 2

            index = -1
            maximum = float("-inf")

            for i in range(m):
                if mat[i][mid] > maximum:
                    maximum = mat[i][mid]
                    index = i

            left = mat[index][mid - 1] if mid > 0 else -1
            right = mat[index][mid + 1] if mid < n - 1 else -1

            if mat[index][mid] > left and mat[index][mid] > right:
                return [index, mid]
            elif mat[index][mid] < left:
                end = mid - 1
            elif mat[index][mid] < right:
                start = mid + 1

        return [-1, -1]
