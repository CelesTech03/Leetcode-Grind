# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return head
        tempStack = []
        temp = head
        while temp:
            tempStack.append(temp.val)
            temp = temp.next
        while head:
            if head.val != tempStack.pop(): 
                return False
            head = head.next
        return True