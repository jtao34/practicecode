# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #step 1: find mid
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        sec_head = slow.next #mid = slow.next
        slow.next = None #disconnect first half and second half
        #step 2: reverse second half
        pre = None 
        cur = sec_head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        #step 3: sum twins
        max_sum = 0
        while pre:
            max_sum = max(max_sum, pre.val+head.val)
            pre = pre.next
            head = head.next
        return max_sum