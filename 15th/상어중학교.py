# 구현
import sys
sys.stdin = open('15th\\input','r')
dy = (1,0,-1,0)
dx = (0,1,0,-1)
N, M = map(int, input().split())
global board
board = [list(map(int,input().split())) for _ in range(N)]
global visited
visited = []
global scroe
score = 0

# 블록덩어리를 찾는 BFS 함수
def BFS(color, coordinate):
    global board, visited
    local_visited = []
    group = []
    q = []
    q.append(coordinate)
    row = coordinate[0]
    column = coordinate[1]
    size = 0
    rainbow = 0
    while q:
        start = q.pop()
        y, x = start
        local_visited.append(start)
        group.append(start)
        size += 1
        for i in range(4):
            nxt_y = y+dy[i]
            nxt_x = x+dx[i]
            if 0<=nxt_y<=N-1 and 0<=nxt_x<=N-1:
                if (nxt_y,nxt_x) not in local_visited and board[nxt_y][nxt_x] in [0,color]:
                    local_visited.append((nxt_y,nxt_x))
                    if board[nxt_y][nxt_x] == 0:
                        rainbow += 1
                    else:
                        if nxt_y < row:
                            row = nxt_y
                            column = nxt_x
                        elif nxt_y == row:
                            if nxt_x < column:
                                column = nxt_x
                                row = nxt_y
                    if board[nxt_y][nxt_x] == color:
                        visited.append((nxt_y,nxt_x))
                    q.append((nxt_y,nxt_x))
    return [size, rainbow, row, column, group]
# 가장 큰 블록 덩어리를 찾아서 지우고, 점수를 더하는 함수
def func1():
    global board, visited, score
    row = -1
    column = -1
    size = 0
    rainbow = 0
    biggist = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 or board[i][j] == -1 or board[i][j] == 'g' :
                continue
            if (i,j) in visited:
                continue
            color = board[i][j]
            group = BFS(color,(i,j))
            if group[0] >size:
                biggist = group[4]
                size = group[0]
                rainbow = group[1]
                row = group[2]
                column = group[3]
            elif group[0] == size:
                if group[1]>rainbow:
                    biggist = group[4]
                    rainbow = group[1]
                    row = group[2]
                    column = group[3]
                elif group[1] == rainbow:
                    if group[2] > row:
                        biggist = group[4]
                        row = group[2]
                        column = group[3]
                    elif group[2] == row:
                        if group[3] > column:
                            biggist = group[4]
                            column = group[3]
                            row = group[2]       
    if size <=1:
        print(score)
        sys.exit(0)
    for block in biggist:
        y,x = block
        board[y][x] = 'g'
    score += size**2
# 중력을 적용하는 함수
def gravity():
    global board
    for i in range(N-1,0,-1):
        for j in range(N):
            if board[i][j] == 'g':
                for k in range(i-1,-1,-1):
                    if board[k][j] == -1:
                        break
                    if board[k][j] != 'g':
                        board[k][j], board[i][j] = board[i][j], board[k][j]
                        break
# 반시계방향으로 90도 회전하는 함수
def rotate():
    global board
    board = [[board[N-j-1][i] for j in range(N-1,-1,-1)] for i in range(N-1,-1,-1)]

while True:
    func1()
    gravity()
    rotate()
    gravity()
    visited.clear()
