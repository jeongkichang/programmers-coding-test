from solution import solution

def run_test_cases():
    test_cases = [
        {"input": (2, 9), "expected": [4, 5]},
        {"input": (2, 1), "expected": [-1]},
        {"input": (2, 8), "expected": [4, 4]},
    ]

    for i, test in enumerate(test_cases):
        input_n, input_s = test["input"]
        expected = test["expected"]
        result = solution(input_n, input_s)
        
        if result == expected:
            print(f"테스트 {i + 1}\n입력값 〉\t{input_n}, {input_s}\n기댓값 〉\t{expected}\n실행 결과 〉\t테스트를 통과하였습니다.\n")
        else:
            print(f"테스트 {i + 1}\n입력값 〉\t{input_n}, {input_s}\n기댓값 〉\t{expected}\n실행 결과 〉\t테스트를 통과하지 못하였습니다.\n결과값 〉\t{result}\n")

if __name__ == "__main__":
    run_test_cases()