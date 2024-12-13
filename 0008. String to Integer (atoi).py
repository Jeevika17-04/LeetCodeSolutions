class Solution(object):
    def myAtoi(self, s):
        s1="0"
        p=0
        digit=False
        for i in s:
            if i=='-' and p==0 and not digit:
                p=1
            elif (i=='+' and p==0 and not digit) :
                p=2
            elif (i==" " and not digit and p==0) :
                continue
            elif i.isdigit():
                s1+=i
                digit=True
            else:
                break
        n=int(s1)
        if p==1:
            n=-n
        if n>=2**31:
            n=(2**31)-1
        elif n<(-2**31):
            n=-2**31
        return n
        
