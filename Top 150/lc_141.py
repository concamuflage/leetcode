from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next

        while slow is not fast and fast is not None:
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next
        if slow is fast:
            return True 
        else:
            return False 



        