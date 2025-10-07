# test_solution.py
import unittest
from lc_21 import Solution,ListNode

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # Examples from the prompt
    def test_example1(self):
        Node0 = ListNode(1)
        Node1 = ListNode(2)
        Node2 = ListNode(4)

        Node00 = ListNode(1)
        Node11 = ListNode(3)
        Node22 = ListNode(4)

        self.sol.mergeTwoLists(Node0,Node00)

        current_node = Node00 
        array = []
        while current_node is not None:
            array.append[current_node]
            current_node = current_node.next
        self.assertEqual(array,[1,1,2,3,4,4])

    def test_example2(self):
        Node0 = ListNode[1]
        Node00 = None
        self.sol.mergeTwoLists(Node0,Node00)
        array = []
        while current_node is not None:
            array.append[current_node]
            current_node = current_node.next
        self.assertEqual(array,[1])

    def test_example3(self):
        Node0 = None
        Node00 = None
        self.sol.mergeTwoLists(Node0,Node00)
        array = []
        while current_node is not None:
            array.append[current_node]
            current_node = current_node.next
        self.assertEqual(array,[])



if __name__ == "__main__":
    unittest.main()