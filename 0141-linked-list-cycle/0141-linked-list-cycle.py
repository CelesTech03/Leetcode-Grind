# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        if not head or not head.next:
            return False
        
        slow = head.next
        fast = head.next.next
        
        while fast and fast.next:
            if slow == fast or fast.next == slow:
                return True
            slow = slow.next
            fast = fast.next.next
            
        return False

        
#         if not head or not head.next:
#             return False
        
#         slow = head
#         fast = head.next
        
#         while fast and fast.next:
#             if fast == slow or fast.next == slow:
#                 return True
#             slow = slow.next
#             fast = fast.next.next
#         return False