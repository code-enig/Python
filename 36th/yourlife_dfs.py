import sys
from collections import defaultdict
sys.setrecursionlimit(200000)
sys.stdin = open('input','r')
n,m = map(int,sys.stdin.readline().split())
situatoin_inf = defaultdict(list)
visited = [False for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    situatoin_inf[x].append(y) 

INF = float('inf')
memo = [INF for _ in range(n+1)] # 그 상황에서 꿈까지 도달하는데 걸리는 변화의 수를 담을 배열
memo[n] = 0 # 이미 꿈이라면 변화가 필요 없으므로
def dfs(k):
    if memo[k] != INF: # 이미 찾은 값이 있다면 그 값을 반환한다.
        return memo[k]
    ret = INF
    for nxt in situatoin_inf[k]: # 이 다음에 올 모든 상황들에 대하여
        ret = min(dfs(nxt)+1,ret) # 이 상황에선 이 다음 상황에서 꿈까지 가는 변화의 수+1 만큼 변화의 수가 필요하므로
    memo[k] = ret # 그 변화의 수를 기록해둔다.
    return ret

answer = dfs(1)

print(answer if answer!= INF else -1)