class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        ind = 0
        while temp:
            temp = temp.next
            ind += 1
        
        n = ind - n - 1 
        temp = head
        
        while n > 0 and temp.next:
            temp = temp.next
            n -= 1
        
        if temp.next and n == 0:
            temp.next = temp.next.next
            return head

        return head.next
