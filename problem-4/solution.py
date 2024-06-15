import math

def solution(k, d):
    available_count = 0
    
    for a in range(0, d + 1, k):
        max_b_square = d ** 2 - a ** 2
        if max_b_square >= 0:
            max_b = int(math.sqrt(max_b_square))
            available_count += (max_b // k) + 1
    
    return available_count
