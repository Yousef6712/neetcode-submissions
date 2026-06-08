# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       
        Slow = head
        Fast = head

        while Fast != None and Fast.next != None:
            Fast = Fast.next.next
            Slow = Slow.next

            if Slow == Fast:
                return True

        return False

        