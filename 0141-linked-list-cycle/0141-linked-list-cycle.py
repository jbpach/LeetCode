# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        passed = []
        current = head
        while current:
            if current not in passed:
                passed.append(current)
            else:
                return True
            current = current.next
        return False
        