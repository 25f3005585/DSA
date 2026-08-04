class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        count = 1
        index = 1

        for i in range(1, n):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                if count > 1:
                    if count < 10:
                        chars[index] = str(count)
                        index += 1
                    else:
                        string = str(count)
                        for j in range(len(string)):
                            chars[index] = string[j]
                            index += 1

                if index != i:
                    chars[index] = chars[i]
                index += 1
                count = 1

        if count > 1:
            if count < 10:
                chars[index] = str(count)
                index += 1
            else:
                string = str(count)
                for j in range(len(string)):
                    chars[index] = string[j]
                    index += 1

        return index
