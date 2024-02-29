import unittest
from my_answer.zigzag_conversion import Solution

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        input_s = "PAYPALISHIRING"
        input_numRows = 3
        expected_output = "PAHNAPLSIIGYIR"
        actual_output = self.solution.convert(input_s, input_numRows)
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        input_s = "PAYPALISHIRING"
        input_numRows = 4
        expected_output = "PINALSIGYAHRPI"
        actual_output = self.solution.convert(input_s, input_numRows)
        self.assertEqual(actual_output, expected_output)

    def test_case3(self):
        input_s = "A"
        input_numRows = 1
        expected_output = "A"
        actual_output = self.solution.convert(input_s, input_numRows)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()