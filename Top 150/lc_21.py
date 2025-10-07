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
        # neither of the two lists is empty,splice them
        
        current_node_1 = list1
        current_node_2 = list2
        next_current_node_1 = list1.next
        next_current_node_2 = list2.next


        while current_node_1.next is not None and current_node_2.next is not None:
                # in each iteration, 3 values are going to be compared.
                # current_node_2,current_node_1, and the smaller node's next node
                # splice list2 into list1
                smaller = current_node_1
                bigger = current_node_2
                current_node_2 = current_node_2.next
                current_node_1 = current_node_1.next
                smaller_next = smaller.next


                end.next = smaller
                end = bigger

            else:
                # splice list1 into list2
    
    def compare_first_three_nodes(node1:ListNode, node2:ListNode) -> ListNode:
        # this function take 2 nodes 
        # then it compares node1, node2, and the next node of min(node1,node2)
        # it generates a list of 2
        # returns the correct tail.

        current_node_1 = node1
        current_node_2 = node2

        if node1.val < node2.val:
            smaller = node1
            bigger = node2
        else: 
            smaller = node2
            bigger = node1
        candidate = smaller.next
        if candidate is not None:
            # compare candidate with bigger
            if candidate >= bigger:
                smaller.next = bigger
            
        else:
            smaller.next = bigger  
        tail = smaller.next 

        return tail,current_node_1,current_node_2


            

        



       