# DP[n]
# 1~n-1 번째 건물까지 통신범위에 들어와 있다고 하자.
# n 번째 건물까지 통신범위 안에 포함 시키려면
# 모든 1<=k<=n 인 k에 대해서 다음과 같은 과정을 거쳐서 얻은 통신폭 중 가장 짧은 값을 취하여야 한다.
# 1. n 번째 건물의 x좌표와 n-k 번째 건물의 x 좌표의 차이 또는
# 2. n-k+1 ~ n 번 건물중 가장 높은 건물의 높이 *2 
#   1, 2중에 더 큰 값을 DP[k]에 더 해줘야한다. 
# (k == n 인 경우는 기존 기지국에 연결하기보다 새로 기지국을 짓는것이 싸다는 뜻)
# DP[1~k] + [k+1~n] = DP[n]
import sys
sys.stdin = open('22th\\input','r')
input = sys.stdin.readline
INF = float('inf')
N = int(input())
dp = [INF for _ in range(N+1)]   
xy = [tuple(map(int,input().split())) for _ in range(N)]
xy.sort(key = lambda x: x[0])
dp[0] = 0
for i in range(N+1):
    y_max = 0
    for j in range(i,-1,-1):
        y_max = max(y_max, abs(xy[j-1][1]))
        dp[i] = min(dp[i], dp[j-1]+max(2*y_max, xy[i-1][0]-xy[j-1][0]))
print(dp[-1])