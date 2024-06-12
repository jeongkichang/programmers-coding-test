from solution import solution

def run_test_cases():
    test_cases = [
        {"input": "()()", "expected": True},
        {"input": "(())()", "expected": True},
        {"input": ")()(", "expected": False},
        {"input": "(()(", "expected": False}
    ]

    for i, test in enumerate(test_cases):
        input_s = test["input"]
        expected = test["expected"]
        result = solution(input_s)
        
        if result == expected:
            print(f"테스트 {i + 1}\n입력값 〉\t{input_s}\n기댓값 〉\t{expected}\n실행 결과 〉\t테스트를 통과하였습니다.\n")
        else:
            print(f"테스트 {i + 1}\n입력값 〉\t{input_s}\n기댓값 〉\t{expected}\n실행 결과 〉\t테스트를 통과하지 못하였습니다.\n결과값 〉\t{result}\n")

if __name__ == "__main__":
    run_test_cases()