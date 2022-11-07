import sys
from collections import deque
sys.stdin = open('21th\\input','r')
input = sys.stdin.readline
N,M = map(int, input().split())
visited = [[-1 for _ in range(N+2)]]
for _ in range(M):
    visited.append([-1] + list(map(int,input().split())) + [-1]) # 범위 확인 안하고 방문한걸로 처리해버리도록 -1로 둘러 싼다
visited.append([-1 for _ in range(N+2)])
d = ((1,0),(0,1),(-1,0),(0,-1))
q = deque([])
riped_tomato = 0 # 익은 토마토 갯수
tomato = M*N # 총 토마토 갯수
day = 0

# 한 번 영향을 준 토마토를 다시 방문할 필요는 없다. + 빈칸을 방문할 필요는 없다.
for i in range(1,M+1):
    for j in range(1,N+1):
        if visited[i][j] == 1:
            riped_tomato += 1
            q.append((i,j,day))
        elif visited[i][j] == -1:
            tomato -= 1
#BFS
while q:
    # 사방 확인
    r, c, day = q.popleft()
    if not visited[r+1][c]:
            riped_tomato += 1
            q.append((r+1,c,day+1))
            visited[r+1][c] = 1
    if not visited[r][c+1]:
            riped_tomato += 1
            q.append((r,c+1,day+1))
            visited[r][c+1] = 1
    if not visited[r-1][c]:
            riped_tomato += 1
            q.append((r-1,c,day+1))
            visited[r-1][c] = 1
    if not visited[r][c-1]:
            riped_tomato += 1
            q.append((r,c-1,day+1))
            visited[r][c-1] = 1
    
if riped_tomato == tomato: #모든 토마토가 익었으면
    print(day)
else:
    print(-1)