from sys import stdin
stdin = open("Python\input",'r')
n,m,r,c,k = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]


dice_eyes = [0 for _ in range(6)]
dice_r = [2,1,5]
dice_c = [4,1,3]
bottom = 6
for order in map(int,stdin.readline().split()):
    if order == 1:
        if c + 1 > m - 1: # 명령이 지도 바깥으로 나가는 명령이라면
            continue
        c = c + 1
        dice_c = [bottom, dice_c[0], dice_c[1]] # 전개도 세로 방향 주사위 변화
        bottom = 7-dice_c[1]
        dice_r[1] = dice_c[1]
    elif order == 2:
        if c - 1 < 0:
            continue
        c = c - 1
        dice_c = [dice_c[1], dice_c[2], bottom]
        bottom = 7-dice_c[1]
        dice_r[1] = dice_c[1]
    elif order == 3: 
        if r - 1 < 0:
            continue
        r = r - 1
        dice_r = [dice_r[1],dice_r[2],bottom] #전개도 가로 방향 주사위 변환
        bottom = 7 - dice_r[1]
        dice_c[1] = dice_r[1]
    else:
        if r + 1 > n - 1:
            continue
        r = r + 1 
        dice_r = [bottom,dice_r[0],dice_r[1]]
        bottom = 7 - dice_r[1]
        dice_c[1] = dice_r[1]

    if board[r][c]:
        dice_eyes[bottom-1] = board[r][c]
        board[r][c] = 0
    else:
        board[r][c] = dice_eyes[bottom-1]

    print(dice_eyes[6-bottom])