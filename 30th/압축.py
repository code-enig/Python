# 1. 문자열을 탐색하면서 길이에 +1 한다.()를 하나씩 풀면서 재귀적으로 푼다.
import sys
sys.stdin = open('input','r')
string = sys.stdin.readline().rstrip()

def string_length(s):
    stack = [] # 옆으로 옮겨 담을 스택
    answer = 0 # 모든 압축된 괄호를 풀었을 때 생기는 문자열의 길이
    n_bra = 0 # 괄호가 몇개나 쌓였나
    flag = False # 괄호 바깥인지 안 인지 알려줄 변수
    multi = 1 # 기본 배수
    for i in range(len(s)):
        if flag:
            if s[i] == '(': 
                n_bra += 1 # 브라켓 개수 하나 증가!
                stack.append(s[i])      
            elif s[i] == ')':
                n_bra -= 1 # 브라캣 개수 하나 감소!
                if not n_bra:
                    answer += multi*string_length(stack)
                    stack.clear()
                    flag = False
                    continue
                stack.append(s[i])
            else:
                stack.append(s[i])
        else:
            if s[i] == '(':
                multi = int(s[i-1])
                answer -= 1
                n_bra += 1
                flag = True # 이제부터 ')'를 찾을 준비를 한다.
            else:
                answer += 1
    return answer    

print(string_length(string))