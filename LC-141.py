# https://leetcode.com/problems/linked-list-cycle/description/

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
        
        if head is None:
            return False 
        
        slow = head
        fast = head

        while fast.next and fast.next.next:   
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast: 
                return True 
        
        return False
