# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        binStr = ""
        current = head
        while current:
            binStr = binStr + str(current.val)
            current = current.next
            
        
        return int(binStr, 2)
            

            
        