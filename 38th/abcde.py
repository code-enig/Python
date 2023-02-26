# 높이가 5이상이 트리가 존재하는지?
# BFS
import sys
from collections import deque,defaultdict
sys.stdin = open('Python\\input','r')
n,m = map(int,sys.stdin.readline().split())
friends = defaultdict(list)
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(n):
    visited = [False for _ in range(n)]
    q = deque()
    q.append(i)
    visited[i] = True
    length = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()
            for nxt in friends[now]:
                if not visited[nxt]:
                    q.append(nxt)
                    visited[nxt] = True
        if q:
            length += 1
        if length == 4:
            print(1)
            sys.exit(0)

print(0)
        
