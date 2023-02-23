# BFS
import sys
from collections import deque
sys.stdin = open('input','r')
n,m = map(int, sys.stdin.readline().split())
matrix_map = []
for _ in range(n):
    matrix_map.append(sys.stdin.readline().rstrip())

dr = (1,0,-1,0)
dc = (0,1,0,-1)
visited = [[[False,False] for _ in range(m)] for _ in range(n)] # 벽을 부수고 또는 부수지 않고 방문한 적이 있는지
q = deque()
q.append((0,0,False)) # row, col, 오면서 벽을 부순적이 있는지 
visited[0][0] = [False,True]
distance = 0
if n == 1 and m == 1:
    print(1)
    sys.exit(0)
while q:
    distance += 1
    for _ in range(len(q)):
        r, c, destruction = q.popleft()
        for i in range(4):
            nxt_r = r+dr[i]
            nxt_c = c+dc[i]
            if nxt_r == n-1 and nxt_c == m-1: # 
                print(distance+1)
                sys.exit(0)
            if 0 <= nxt_r < n and 0 <= nxt_c < m:
                if matrix_map[nxt_r][nxt_c] == '0':
                    if not destruction and not visited[nxt_r][nxt_c][1]:
                        q.append((nxt_r,nxt_c,False))
                        visited[nxt_r][nxt_c][1] = True
                    if destruction and not visited[nxt_r][nxt_c][0]:
                        q.append((nxt_r,nxt_c,True))
                        visited[nxt_r][nxt_c][0] = True
                if matrix_map[nxt_r][nxt_c] == '1':
                    if not destruction and not visited[nxt_r][nxt_c][0]:
                        q.append((nxt_r,nxt_c,True))
                        visited[nxt_r][nxt_c][0] = True
print(-1)