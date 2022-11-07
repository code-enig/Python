#절댓값이 큰 수 끼리 곱할수록 커진다. 
# 예외 -> 0 , 1
# 0 은 곱하지 않는 것이 좋다-> 예외) 음수가 홀로 남았다면 곱하는게 유리하다
# 1 은 곱하지 않는 것이 좋다
import sys
sys.stdin = open('21th\\input','r')
input = sys.stdin.readline
N = int(input())
seq = list(int(input()) for _ in range(N))
seq.sort()
s = 0
i = 0
# 가장 큰 음수에서 0 까지 절댓값이 큰 순서대로 짝지어 곱한다.
while i <= len(seq)-2:
    a1,a2 = seq[i],seq[i+1]
    if a1<= -1 and  a2 <= 0:
        s += a1*a2
        i += 2
    else:
        break
# 짝지어지지 않은 홀수가 있다면, 그냥 더한다.
if seq[i] < 0:
    s += seq[i]

j = -1
# 1보다 큰 정수가 떨어지거나 하나 남을 때까지 절댓값이 큰 순서대로 짝지어 곱한다.
while j >= -len(seq)+1:
    a1,a2 = seq[j],seq[j-1]
    if a1 >= 2 and  a2 >= 2 :
        s += a1*a2
        j -= 2
    else:
        break
# 이제 1보다 크거나 같은 남은 정수들을 전부 더 한다.
while j >= -len(seq):
    a1 = seq[j]
    if a1 >= 1:
        s += a1
        j -= 1
    else:
        break
print(s)
