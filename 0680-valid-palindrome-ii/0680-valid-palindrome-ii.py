class Solution:
    def isPalindrome(self,left, right, s):
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return [False,left, right]
        
        return [True,left,right]

    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        if n <= 2:
            return True
        
        i = 0
        j = n - 1

        is_palindrome,left,right = self.isPalindrome(i,j,s)
        if is_palindrome:
            return True
        else:
            i = left + 1
            j = right
            is_palindrome,_,_ = self.isPalindrome(i, j , s)

            if is_palindrome:
                return True

            i = left
            j = right -1

            is_palindrome,_,_ = self.isPalindrome(i, j , s)
            if is_palindrome:
                return True
            
            return False
