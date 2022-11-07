# glass[n] 을 포도주의 양
# DP[n] = [i,j,k] 라 하자 i는 n번째 포도주를 마시지 않을때, j는 첫 잔으로, k는 두번째 잔으로 마실때 최대 총 포도주양이다.
# n번째 포도주에 대해서 3가지 경우의 수가 있다. 
# 1. DP[n][0] = max(DP[n-1])
# 2. DP[n][1] = DP[n-1][0]+glass[n]
# 3. DP[n][2] = DP[n-1][1]+glass[n]
import sys
sys.stdin = open('23th\\input','r')
input = sys.stdin.readline
n = int(input())
DP = [[0,0,0] for _ in range(n)]
first = int(input())
DP[0] = [0,first,first]
for i in range(1,n):
    glass = int(input())
    DP[i][0] = max(DP[i-1])
    DP[i][1] = DP[i-1][0]+glass
    DP[i][2] = DP[i-1][1]+glass
print(max(DP[-1]))