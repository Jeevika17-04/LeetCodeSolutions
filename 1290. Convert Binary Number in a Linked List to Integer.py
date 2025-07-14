class Solution(object):
    def getDecimalValue(self, head):
        temp = head
        c = 0
        while(temp):
            c += 1
            temp = temp.next
        temp = head
        c, s = c - 1, 0
        while(temp):
            s += temp.val * (2**c)
            temp = temp.next
            c -= 1
        return s
