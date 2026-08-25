class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        stack = []
        seen = set()
        arr = [0] * 26

        for i in range(n):
            elem = s[i]
            index = ord(elem) - ord("a")
            arr[index] = i

        for i in range(n):
            elem = s[i]

            if elem in seen:
                continue

            while stack and stack[-1] > elem and i < arr[ord(stack[-1]) - ord("a")]:
                top = stack.pop()
                seen.discard(top)

            stack.append(elem)
            seen.add(elem)

        return "".join(stack)
