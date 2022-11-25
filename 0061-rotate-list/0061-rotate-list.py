# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head

        # Compute the length of the list
        list_len = 1
        counter = head
        while counter.next:
            list_len += 1
            counter = counter.next

        counter.next = head # Make list circular

        k = k % list_len # Calculate new rotate size
        new_end = head
        for _ in range(list_len - k - 1):
            new_end = new_end.next
        new_start = new_end.next
        new_end.next = None
        return new_start