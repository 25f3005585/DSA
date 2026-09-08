class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        number = []
        char = []
        n = len(logs)
        result = [0] * n

        for i in range(n):
            log = logs[i]
            arr = log.split(" ")

            if arr[1].isdigit():
                number.append(log)
            else:
                values = log.split(" ")
                char.append([' '.join(values[1:]), values[0], i])

        result = []

        for log in sorted(char):
            result.append(logs[log[2]])
        
        return result + number

        