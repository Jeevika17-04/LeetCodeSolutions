class Solution(object):
    def reverse(self, x):
        i=0
        s=0
        if x<0:
            x=-x
            s=1
        while x>0:
            i=i*10+x%10
            x//=10
        if i>=2**31 or i<= -2**31:
            return 0
        elif s==1:
            return -i
        return i
