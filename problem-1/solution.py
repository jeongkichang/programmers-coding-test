def solution(n, s):
    # n이 s보다 크면 조합을 만들 수 없습니다.
    if n > s:
        return [-1]

    # 몫과 나머지를 구합니다.
    quotient = s // n
    remainder = s % n
    
    # 기본 몫으로 n개의 요소를 생성합니다.
    answer = [quotient] * n
    
    # 나머지를 분배합니다.
    for i in range(remainder):
        answer[i] += 1
    
    # 오름차순으로 정렬하여 반환합니다.
    return sorted(answer)