import unittest
from my_answer.next_greater_element1 import Solution

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        input_nums1 = [4,1,2]
        input_nums2 = [1,3,4,2]
        expected_output = [-1,3,-1]
        actual_output = self.solution.nextGreaterElement(input_nums1, input_nums2)
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        input_nums1 = [2,4]
        input_nums2 = [1,2,3,4]
        expected_output = [3,-1]
        actual_output = self.solution.nextGreaterElement(input_nums1, input_nums2)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()