from collections import deque
def solution(s):
    answer = 0
    dq = deque([])
    for bracket in s:
        dq.append(bracket)
    for _ in range(len(s)-1):
        print(dq)
        if isRightBracket(dq):
            answer += 1
        dq.rotate(-1)
    return answer
def isRightBracket(s):
    open_stack = []
    open_brackets = ('(', '{', '[')
    close_brackets = (')', '}' , ']')
    close = -1

    if len(s)%2:
        return False  
    for i in range(len(s)):
        for j in range(3):
            if s[i] == open_brackets[j]:
                open_stack.append(j)
            if s[i] == close_brackets[j]:
                close = j
                if not open_stack:
                    return False 
                else:
                    if close == open_stack[-1]:
                        open_stack.pop()
                    else:
                        return False
    return True

s = "[](){}"
print(solution(s))
s = "}]()[{"
print(solution(s))
s = "[)(]"
print(solution(s))
s = "}}}"
print(solution(s))