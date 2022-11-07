def solution(dirs):
    answer = 0
    walked_rows = [[False for i in range(10)] for j in range(11)]
    walked_cols = [[False for i in range(10)] for j in range(11)]
    x,y = 5,5
    for dir in dirs:
        nxt_x, nxt_y = x,y
        if dir == 'U':
            nxt_y += 1
            nxt_col = y
            if nxt_col<10 and not walked_cols[x][nxt_col]:
                walked_cols[x][nxt_col] = True
                answer += 1
        elif dir == 'D':
            nxt_y -=1
            nxt_col = y-1
            if 0<=nxt_col and not walked_cols[x][nxt_col]:
                walked_cols[x][nxt_col] = True
                answer += 1
        elif dir == 'R':
            nxt_x +=1
            nxt_row = x
            if nxt_row<10 and not walked_rows[y][nxt_row]:
                walked_rows[y][nxt_row] = True
                answer += 1
        elif dir == 'L':
            nxt_x -=1
            nxt_row = x-1
            if 0<=nxt_row and not walked_rows[y][nxt_row]:
                walked_rows[y][nxt_row] = True
                answer += 1
        if 0<=nxt_x<11 and 0<=nxt_y<11:
            x, y = nxt_x, nxt_y
    return answer