# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        
        res = []
        temp = head
        while temp != None:
            res.append(temp.val)
            temp = temp.next
        
        res.reverse()

        newHead = ListNode(res[0])
        current = newHead
        
        for i in range(1, len(res)):
            current.next = ListNode(res[i])
            current = current.next
            
        return newHead