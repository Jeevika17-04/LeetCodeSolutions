class Solution(object):
    def isPalindrome(self, x):
        l=[]
        if x<0:
            return False
        while x>0:
            l+=[x%10]
            x//=10
        n=len(l)
        for i in range(n):
            if l[i]!=l[(n-1)-i]:
                return False
        return True
