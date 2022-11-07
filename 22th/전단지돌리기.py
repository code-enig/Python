# DFS의 의미 생각
import sys
from collections import defaultdict
sys.stdin = open('22th\\input','r')

def dfs(n,p):
    global d
    d_max = 0
    for next in nodes[n]:
        if next != p : # 트리 형태이므로
            d_max = max(d_max,dfs(next,n))
    if d_max >= D:
        d += 1
    print(n,d_max)
    return d_max+1

input = sys.stdin.readline
N,S,D = map(int,input().split())
global d # 이동거리
nodes = defaultdict(list)
for _ in range(N-1):
    x,y = map(int, input().split())
    nodes[x].append(y)
    nodes[y].append(x)
d=0
dfs(S,0)
print(2*(d-1) if d else 0)