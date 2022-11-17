# glass[n] 을 포도주의 양
# dp[n] = [i,j,k] 라 하자 i는 n번째 포도주를 마시지 않을때, j는 첫 잔으로, k는 두번째 잔으로 마실때 총 포도주양 최댓값이다.
# n번째 포도주에 대해서 3가지 경우의 수가 있다. 
# 1. dp[n][0] = max(dp[n-1])
# 2. dp[n][1] = dp[n-1][0]+glass[n]
# 3. dp[n][2] = dp[n-1][1]+glass[n]
import sys
sys.stdin = open('23th\\input','r')
input = sys.stdin.readline
n = int(input())
dp = [[0,0,0] for _ in range(n)]
first = int(input())
dp[0] = [0,first,first]
for i in range(1,n):
    glass = int(input())
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0]+glass
    dp[i][2] = dp[i-1][1]+glass
print(max(dp[-1]))