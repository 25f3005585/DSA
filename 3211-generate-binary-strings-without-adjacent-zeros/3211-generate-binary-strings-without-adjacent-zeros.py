class Solution:
    def generateStrings(self, string, arr, n):
        if len(string) == n:
            arr.append("".join(string))
            return

        if len(string) and string[len(string)-1] != '0':
            string.append("0")
            self.generateStrings(string, arr, n)
            string.pop()
        
        if len(string) == 0:
            string.append("0")
            self.generateStrings(string, arr, n)
            string.pop()

        string.append("1")
        self.generateStrings(string, arr, n)
        string.pop()
        return

    def validStrings(self, n: int) -> List[str]:
        arr = []
        string = []
        self.generateStrings(string, arr, n)
        return arr
