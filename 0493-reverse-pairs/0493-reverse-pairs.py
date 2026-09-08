class Solution:
    def merge(self, arr, start, mid, end):
        temp = []
        i = start
        j = mid + 1
        count = 0
        right = mid + 1

        for idx in range(start, mid + 1):
            while right <= end and arr[idx] > (2 * arr[right]):
                right+=1
            
            count += (right - (mid + 1))

        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= end:
            temp.append(arr[j])
            j += 1

        for index in range(start, end + 1):
            arr[index] = temp[index - start]

        return count

    def mergeSort(self, arr, start, end):
        if start >= end:
            return 0

        mid = (start + end) // 2
        count = 0
        count += self.mergeSort(arr, start, mid)
        count += self.mergeSort(arr, mid + 1, end)
        count += self.merge(arr, start, mid, end)
        return count

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)
