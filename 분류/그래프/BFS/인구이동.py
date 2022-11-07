# BFS
# 이미 연합국이었던 곳을 또 다시 탐색할 필요는 없다.
# 만약 전날 연합국을 이뤘던 나라가 아니라면 인구이동이 일어나지 않았으므로 
# 그 주변 국가에서 인구이동이 일어난게 아니라면 다시 연합국을 형성할 가능성이 없다.
# 따라서 그 국가에서는 탐색을 시작하지 않는다. 이렇게 하더라도 인구이동이 일어난 다른 나라에서 그 나라로의 탐색은 가능하므로
# 제외되는 경우는 없다.
  
import sys
from collections import deque
sys.stdin = open('20th\\input','r')
input = sys.stdin.readline
N,L,R = map(int,input().split())
pop_mat = [list(map(int,input().split())) for _ in range(N)]

dr = (1,0,-1,0)
dc = (0,1,0,-1)
visited = [[-1 for i in range(N)] for j in range(N)] # 오늘(day) BFS 탐색중에 방문했는지 알려줄 배열 
country_list = deque([(i,j) for i in range(N) for j in range(N)]) # 연합국을 이루는 순서대로 들어간 국가 데크

for day in range(0, 2001):
    q= deque()
    length = len(country_list)
    for _ in range(length):
        i, j = country_list.popleft()
        if visited[i][j] == day:
            continue
        visited[i][j] = day
        union = set([(i,j)])
        pop = pop_mat[i][j]
        q.append((i,j))

        while q:
            r,c = q.popleft()
            for k in range(4):
                nxt_r = r + dr[k]
                nxt_c = c + dc[k]
                if 0<=nxt_r<N and 0<=nxt_c<N and visited[nxt_r][nxt_c] != day and L<=abs(pop_mat[nxt_r][nxt_c]-pop_mat[r][c])<=R:
                    visited[nxt_r][nxt_c] = day
                    pop += pop_mat[nxt_r][nxt_c]
                    union.add((nxt_r,nxt_c))
                    q.append((nxt_r,nxt_c))
        
        if len(union) > 1:
            avg = pop//len(union)
            for r,c in union:
                pop_mat[r][c] = avg
                country_list.append((r,c)) 
                # 이렇게 하면 인구이동이 일어났던 나라들만 순서대로 담기고 인구이동이 일어난 나라가 없을경우 빈 데크가 남는다.
    if not country_list:
        break
print(day)