# 왼쪽부터 오른쪽으로 좌석에 앉는 2가지 방법이 있다. 제자리에 앉거나 왼쪽과 바꿔 앉거나(오른쪽과 바꿔 앉는 것은 다음 자리로가서 생각하면 된다.)
import sys
sys.stdin = open('Python\\25th\\input','r')
input = sys.stdin.readline
N = int(input())
M = int(input())
answer = 1
global left
left = 0

def dp(right,a):
    b = a
    global left
    cases = [[0,0] for _ in range(right-left)]
    if cases:
        cases[0] = [1,0]# 제자리에 앉을 때 가짓수를 cases[][0] 바꿔 앉을 때를 cases[][1] 이라 하자
        for i in range(1,len(cases)):
            cases[i][0] = cases[i-1][0] + cases[i-1][1] # 왼쪽 자리 사람이 바꿔 앉았든 제자리에 앉았든 제자리에는 앉을 수 있다.
            cases[i][1] = cases[i-1][0] # 왼쪽 자리 사람이 제자리에 앉았을 때만 바꿔 앉을 수 있다.
        b *= sum(cases[-1])
    left = right+1
    return b

for _ in range(M):
    answer = dp(int(input())-1, answer)
answer = dp(N,answer)
print(answer)