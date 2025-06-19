class Solution(object):
    def removeKdigits(self, num, k):
        n = len(num)
        stack = []
        
        for digit in num:
            while stack and digit < stack[-1] and k > 0:
                stack.pop(-1)
                k -= 1
            stack.append(digit)
        
        while k > 0 and stack:
            stack.pop(-1)
            k -= 1
        
        number = ""
        n = len(stack)

        temp = ""
        for i in range(n):
            val = stack.pop(-1)
            
            if val == "0":
                temp += "0" 
            else:
                number = val + temp + number
                temp = ""
        
        return number if number else "0"
        
