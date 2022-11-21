# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        
        while l1 or l2 or carry:
            # Value 1 = List 1 value if non-empty, else 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit
            val = v1 + v2 + carry
            # 15
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
            
        
        
        
#         dummy = curr = ListNode()
#         carryover = 0
        
#         while l1 or l2:
#             d = carryover
#             if l1 and l2:
#                 d += (l1.val + l2.val)
#                 l1 = l1.next
#                 l2 = l2.next
#             elif l1:
#                 d += l1.val
#                 l1 = l1.next
#             elif l2:
#                 d += l2.val
#                 l2 = l2.next
#             carryover = d // 10
#             curr.next = ListNode(d%10)
#             curr = curr.next
#         if carryover == 1:
#             curr.next = ListNode(1)
#         return dummy.next
         
#         n1, n2 = "", ""
        
#         while l1:
#             n1 = str(l1.val) + n1
#             l1 = l1.next
#         while l2:
#             n2 = str(l2.val) + n2
#             l2 = l2.next
        
#         if not n1:
#             n1 = 0
#         if not n2:
#             n2 = 0
#         summ = int(n1) + int(n2)
        
#         dummy = curr = ListNode()
#         for i in reversed(str(summ)):
#             curr.next = ListNode(int(i))
#             curr = curr.next
#         return dummy.next
            