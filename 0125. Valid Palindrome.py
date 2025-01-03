class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        i , j = 0, len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
            elif not s[j].isalnum():
                j -= 1
                continue
            
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        return True
