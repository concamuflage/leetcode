from copy import copy
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        list1_pointer = list1
        list2_pointer = list2
        if list2_pointer.val <= list1_pointer.val:
            head = list2_pointer
            list2_pointer = list2_pointer.next
        else:
            head = list1_pointer
            list1_pointer = list1_pointer.next
        prev = head

        while list2_pointer is not None and list1_pointer is not None:
            if list2_pointer.val == list1_pointer.val:
                prev.next = list2_pointer
                prev = prev.next
                list2_pointer = list2_pointer.next

                prev.next = list1_pointer
                prev = prev.next
                list1_pointer = list1_pointer.next

            elif list2_pointer.val < list1_pointer.val:
                prev.next = list2_pointer
                list2_pointer = list2_pointer.next
                prev = prev.next

            else:
                prev.next = list1_pointer
                list1_pointer = list1_pointer.next
                prev = prev.next
        if list1_pointer is not None:
            prev.next = list1_pointer
        if list2_pointer is not None:
            prev.next = list2_pointer
        return head





            

        



       