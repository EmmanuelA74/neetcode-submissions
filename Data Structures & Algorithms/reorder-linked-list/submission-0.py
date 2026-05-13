# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split in half, reverse second half, then merge back

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None    #sever first half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        first, second = head, prev
        while second:
            first_nxt = first.next
            second_nxt = second.next
            first.next = second
            second.next = first_nxt
            first = first_nxt
            second = second_nxt
        