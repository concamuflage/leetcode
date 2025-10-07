import unittest
from lc_141 import Solution,ListNode  # adjust if your file name is different

sol = Solution()

class TestTwoSum(unittest.TestCase):

    def test_case1(self):
        # construct a list

        node_0 = ListNode(1)
        node_1 = ListNode(2)
        node_2 = ListNode(0)
        node_3 = ListNode(-4)

        node_0.next = node_1
        # node_1.next = node_2
        # node_2.next = node_3
        # node_3.next = node_1
        
        self.assertFalse(sol.hasCycle(node_0))


if __name__ == "__main__":
    unittest.main(verbosity=2)