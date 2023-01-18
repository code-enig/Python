import sys
from collections import deque
sys.stdin = open('input','r')
n,m = map(int, sys.stdin.readline().split())
d_paper = [[0 for _ in range(m+2)]]
d_paper.extend([[0]+list(map(int, sys.stdin.readline().split()))+[0] for _ in range(n)])
d_paper.append([0 for _ in range(m+2)])

q = deque()
visited = [[0 for _ in range(m+2)] for _ in range(n+2)]
d_count =  0 # 그림의 갯수
d_max_size = 0 # 최대 그림넓이
for i in range(1,n+1):
    for j in range(1,m+1):
        if d_paper[i][j] == 1:
            d_count += 1
            d_size = 0
            d_paper[i][j] = 0 # 이미 탐색한 그림은 0 으로 바꿔 다시 탐색하지 않도록 한다.
            visited[i][j] = d_count # 이게 몇번쨰 그림의 방문인지 기록한다.
            q.append((i,j))
            while q:
                d_size += 1
                r,c = q.popleft()
                if d_paper[r+1][c] == 1 and visited[r+1][c] != d_count:
                    visited[r+1][c] = d_count
                    d_paper[r+1][c] = 0
                    q.append((r+1,c))

                if d_paper[r][c+1] == 1 and visited[r][c+1] != d_count:
                    visited[r][c+1] = d_count
                    d_paper[r][c+1] = 0
                    q.append((r,c+1))

                if d_paper[r-1][c] == 1 and visited[r-1][c] != d_count:
                    visited[r-1][c] = d_count
                    d_paper[r-1][c] = 0
                    q.append((r-1,c))

                if d_paper[r][c-1] == 1 and visited[r][c-1] != d_count:
                    visited[r][c-1] = d_count
                    d_paper[r][c-1] = 0
                    q.append((r,c-1))

            d_max_size = max(d_max_size, d_size)
            
print(d_count, d_max_size)
                    
