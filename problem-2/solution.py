def solution(s):
    first_char = s[0]
    count_left = s.count('(')
    count_right = s.count(')')
    
    if first_char != '(' :
        return False
    if count_left != count_right :
        return False

    return True