def solution(grid):
    global board
    board = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    global d
    d = ((1,0),(0,-1),(-1,0),(0,1))
    answer = []
    # 그 위치에서 그 방향으로 만든 사이클을 정답에 추가했는지 알려주는 배열
    check_board = [[[0,0,0,0] for _ in range(len(grid[i]))] for i in range(len(grid))]
    # 그 위치를 그 방향으로 통과했는지, 통과 했다면 그리드를 몇개나 거쳐왔는지 담는 배열
    tmp_check_board = [[[0,0,0,0] for _ in range(len(grid[i]))] for i in range(len(grid))] 
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            way_length = 0
            origin = [y,x]
            # 여태까지 지나온 그리드 정보를 담을 스택
            stack = [(y,x)]
            for k in range(4):
                idx = k
                y,x = origin
                while True:
                    way_length += 1
                    x += d[idx][1]
                    y += d[idx][0]
                    if y>len(grid)-1:
                        y = 0
                    elif y<0:
                        y = len(grid)-1

                    if x>len(grid[y])-1:
                        x = 0
                    elif x<0:
                        x = len(grid[y])-1
                    # 다음 방향
                    idx = nxt_idx(y,x,idx)
                    # 위치 스택에 추가
                    stack += [(y,x,idx)]
                    if tmp_check_board[y][x][idx]:
                        if not check_board[y][x][idx]:
                            cycle_length = way_length - tmp_check_board[y][x][idx]
                            pos = tmp_check_board[y][x][idx]
                            while pos <= way_length-1:
                                tmp_y,tmp_x,idx = stack[pos]
                                check_board[tmp_y][tmp_x][idx] = cycle_length
                                pos += 1
                            answer.append(cycle_length)
                            break
                        else:
                            break
                    else:
                        tmp_check_board[y][x][idx] = way_length
                    
        answer.sort()    
    return answer

def nxt_idx(y,x,idx):
    r = board[y][x]

    if r == "R":
        idx = (idx+1)%4
    elif r == "L":
        idx = (idx-1)%4

    return idx

grid = ["S"]

print(solution(grid))