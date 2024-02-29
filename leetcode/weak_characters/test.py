import unittest
from my_answer.weak_characters import Solution

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        input_data = [[5,5],[6,3],[3,6]]
        expected_output = 0
        actual_output = self.solution.numberOfWeakCharacters(input_data)
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        input_data = [[2,2],[3,3]]
        expected_output = 1
        actual_output = self.solution.numberOfWeakCharacters(input_data)
        self.assertEqual(actual_output, expected_output)

    def test_case3(self):
        input_data = [[1,5],[10,4],[4,3]]
        expected_output = 1
        actual_output = self.solution.numberOfWeakCharacters(input_data)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()