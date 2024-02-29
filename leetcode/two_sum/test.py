import unittest
from my_answer.two_sum import Solution

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        input_nums = [2,7,11,15]
        input_target = 9
        expected_output = [0,1]
        actual_output = self.solution.twoSum(input_nums, input_target)
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        input_nums = [3,2,4]
        input_target = 6
        expected_output = [1,2]
        actual_output = self.solution.twoSum(input_nums, input_target)
        self.assertEqual(actual_output, expected_output)

    def test_case3(self):
        input_nums = [3,3]
        input_target = 6
        expected_output = [0,1]
        actual_output = self.solution.twoSum(input_nums, input_target)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()