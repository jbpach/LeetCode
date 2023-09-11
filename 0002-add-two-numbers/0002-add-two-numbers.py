# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        current = dummy
        carry = 0;
        
        currl1 = l1
        currl2 = l2
        
        while currl1 or currl2 or carry:
            val1 = currl1.val if currl1 else 0
            val2 = currl2.val if currl2 else 0
            
            total = val1 + val2 + carry
            
            carry = total // 10
            
            current.next = ListNode(total % 10)
            
            current = current.next
            
            if currl1:
                currl1 = currl1.next
            if currl2:
                currl2 = currl2.next
            
        return dummy.next

            
            
                
            
            
        