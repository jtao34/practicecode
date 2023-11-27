# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first_odd = head
        first_even = head.next
        evenhead = first_even
        while first_even and first_even.next:
            first_odd.next = first_odd.next.next
            first_odd = first_odd.next
            first_even.next = first_even.next.next
            first_even = first_even.next
        first_odd.next = evenhead
        return head