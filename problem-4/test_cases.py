import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution(2, 4), 6)  # (0,0), (0,2), (0,4), (2,0), (2,2), (4,0)
    
    def test_case_2(self):
        self.assertEqual(solution(1, 5), 26)  # 모든 조합 (0,0)부터 (5,0), (0,5)까지
    
    def test_case_3(self):
        self.assertEqual(solution(1, 1), 3)  # (0,0), (0,1), (1,0)
    
    def test_case_4(self):
        self.assertEqual(solution(3, 10), 13)
    
    def test_case_5(self):
        self.assertEqual(solution(2, 1), 1)  # (0,0) only

    def test_case_6(self):
        self.assertEqual(solution(5, 25), 26)  # Detailed calculation: (0,0), (0,5), (0,10), (0,15), (0,20), (0,25), (5,0), (5,5), (5,10), (5,15), (5,20), (10,0), (10,5), (10,10), (10,15), (15,0), (15,5), (15,10), (20,0), (20,5), (25,0), (5,25), (10,20), (15,15), (20,10), (25,5)
    
    def test_case_7(self):
        self.assertEqual(solution(100, 1000000), 78549764)  # 매우 큰 입력 값
    
if __name__ == '__main__':
    unittest.main()
