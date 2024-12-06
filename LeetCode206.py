# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next # sets temp ptr to the next node
            curr.next = prev # sets address to curr to prev node (should be behind curr)
            prev = curr # prev is set to curr
            curr = temp # curr is set to temp
            #basically prev and curr are just bumped up for next iteration
        return prev
        