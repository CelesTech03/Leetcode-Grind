# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        a_nodes = set()
        temp_a = headA
        temp_b = headB
        
        while temp_a:
            a_nodes.add(temp_a)
            temp_a = temp_a.next
            
        while temp_b:
            if temp_b in a_nodes:
                return temp_b
            temp_b = temp_b.next
        return None