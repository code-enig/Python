# 다익스트라
# 방 하나를 노드라고 생각하고 노드끼리 거리가 0인 경우는 1 1인 경우는 0 으로 생각하여 최단거리를 계산
import sys
import heapq
N = int(sys.stdin.readline())
INF = float('inf')
answer = N*N
board = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
num_walls = [[N*N for i in range(N)] for j in range(N)]  #그 곳 까지 도달하는데 부숴야할 벽의 최소 갯수

dx = [1,0,-1,0]
dy = [0,1,0,-1]

start = (0,0)
# 다익스트라 알고리즘
q = []
heapq.heappush(q,(0, start))
num_walls[0][0] = 0
flag = False
while q:
    walls, (y,x) = heapq.heappop(q)
    if num_walls[y][x] < walls:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny <= N-1 and 0 <= nx <= N-1:
            tmp = num_walls[y][x] + (0 if board[ny][nx] else 1)
            if tmp < num_walls[ny][nx]:
                num_walls[ny][nx] = tmp
                # 찾으면 탈출
                if (ny,nx) == (N-1,N-1):
                    print(num_walls[N-1][N-1])
                    sys.exit(0)
                heapq.heappush(q, (num_walls[ny][nx], (ny,nx)))