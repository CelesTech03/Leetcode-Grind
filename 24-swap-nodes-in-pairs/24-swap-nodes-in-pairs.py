# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = curr = ListNode(0)
        curr.next = head
        
        while curr.next and curr.next.next:
            
            slow = curr.next
            fast = curr.next.next
            curr.next, slow.next, fast.next = fast, fast.next, slow
            curr = slow
        return dummy.next
            