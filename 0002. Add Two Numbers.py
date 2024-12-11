# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp=l1
        num1=""
        num2=""
        while temp:
            num1=str(temp.val)+num1
            temp=temp.next
        temp=l2
        while temp:
            num2=str(temp.val)+num2
            temp=temp.next
        num1=int(num1)
        num2=int(num2)
        ans=num1+num2
        head=ListNode(ans%10)
        ans//=10
        tail=head
        while ans:
            temp=ListNode(ans%10)
            ans//=10
            tail.next=temp
            tail=temp
        return head
        
