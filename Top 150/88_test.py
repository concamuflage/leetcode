import unittest
from lc_88 import Solution

sol = Solution()

class Test88(unittest.TestCase):
    
    def test_one(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        sol.merge(nums1,3,nums2,3)
        self.assertEqual(nums1,[1,2,2,3,5,6])
    
    def test_two(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        sol.merge(nums1,m,nums2,n)
        self.assertEqual(nums1,[1])

    def test_three(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        sol.merge(nums1,m,nums2,n)
        self.assertEqual(nums1,[1])


if __name__ == '__main__':
    unittest.main(verbosity=2)