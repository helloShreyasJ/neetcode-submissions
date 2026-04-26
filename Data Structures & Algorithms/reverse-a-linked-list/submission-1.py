# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return

        prev = None
        curr = head

        # understanding this codeblock helped me understand this better
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
    
        return prev