# 최소힙을 활용한 데이크스트라 알고리즘
import sys
from collections import defaultdict
import heapq
sys.stdin = open('Python\\25th\\input','r')
input = sys.stdin.readline
n,m,r = map(int, input().split())
items = list(map(int, input().split()))
roads = defaultdict(list)
for _ in range(r):
    a,b,l = map(int, input().split())
    roads[a-1].append((b-1,l))
    roads[b-1].append((a-1,l))
INF = float('inf')

answer = 0
ini_dist = [INF for _ in range(n)]
for i in range(n): # 출발지를 바꿔가며 데이크스트라 알고리즘을 적용한다.
    dist = ini_dist.copy()
    dist[i] = 0
    q = []
    for p,d in roads[i]: # 최초 노드에서 
        dist[p] = d
        heapq.heappush(q,(d,p))
    while q: # 더이상 갱신할 노드가 없을 때까지
        dis_now,pos_now = heapq.heappop(q) # 가장 가까운 노드를 꺼내온다.
        for p,d in roads[pos_now]:
            if dist[p] > dis_now + d:
                dist[p] = dis_now + d
                heapq.heappush(q,(dist[p],p))
    tmp = 0   
    for j in range(n):
        if dist[j] <= m:
            tmp += items[j]
    answer = max(answer, tmp)

print(answer)