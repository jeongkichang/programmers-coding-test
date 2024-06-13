import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        jobs = [[0, 3], [1, 9], [2, 6]]
        self.assertEqual(solution(jobs), 9)

    def test_case_2(self):
        jobs = [[0, 1], [1, 2], [2, 3]]
        self.assertEqual(solution(jobs), 2)

    def test_case_3(self):
        jobs = [[0, 5], [1, 2], [5, 5]]
        self.assertEqual(solution(jobs), 6)

    def test_case_4(self):
        jobs = [[0, 10], [4, 10], [5, 11]]
        self.assertEqual(solution(jobs), 17)

    def test_case_5(self):
        jobs = [[0, 3], [4, 3], [8, 3]]
        self.assertEqual(solution(jobs), 3)

    def test_case_6(self):
        jobs = [[0, 1]]
        self.assertEqual(solution(jobs), 1)

    def test_case_7(self):
        jobs = [[0, 2], [2, 2], [4, 2]]
        self.assertEqual(solution(jobs), 2)

    def test_case_8(self):
        jobs = [[0, 6], [1, 4], [2, 3], [3, 2]]
        self.assertEqual(solution(jobs), 8)

    def test_case_9(self):
        jobs = [[1, 10], [3, 3], [10, 2]]
        self.assertEqual(solution(jobs), 8)

if __name__ == "__main__":
    unittest.main()
