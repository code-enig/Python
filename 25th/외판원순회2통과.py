import sys
sys.stdin = open('Python\\25th\\input','r')
input = sys.stdin.readline
N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]
INF = float('inf')

dp = [[0 for i in range(1<<N)] for j in range(N)]

def TSP(n,s,v): # {v} 에서 도시 n에서 출발도시(s)로 돌아오는 최소비용경로
    if dp[n][v] :
        return dp[n][v] # 찾아놓은 DP 값 활용
    
    if v == (1<<N)-1: # 모든 도시를 방문 했는데, 
        if W[n][s] > 0: # 거기서 다시 최초 위치로 돌아올수 있다면,
            return W[n][s] # 그 때 비용 반환
        return INF # 아니면 무한대 반환


    min_cost = INF
    for i in range(N): # 없다면 찾는다.
        if W[n][i] == 0:
            continue
        if (1<<i) & v :
            continue
        # 갈수 없거나, 이미 방문한 지역을 제외하고
        min_cost = min(min_cost,W[n][i] + TSP(i,s,v|(1<<i)))
        # 현재 도시에서 다음 도시로 간 뒤 출발 도시로 돌아가는 최소비용들 중 최소비용을
        # 현재 도시에서 출발 도시로 돌아가는 최소비용으로 저장한다.
    dp[n][v] = min_cost
    return dp[n][v]

print(TSP(N//2,N//2,1<<N//2)) # 아무곳에서 출발해도 되므로 가운데쯤에서 출발해보자