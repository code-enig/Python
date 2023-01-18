import random
import os
import time
import msvcrt

p1 = (((0,1),(1,1),(2,1),(3,1)),((2,0),(2,1),(2,2),(2,3)),((0,2),(1,2),(2,2),(3,2)),((1,0),(1,1),(1,2),(1,3))) # ㅣ
p2 = (((0,0),(1,0),(0,1),(1,1)),) # ㅁ
p3 = (((-1,-1),(-1,0),(0,0),(0,1)),((-1,1),(0,1),(0,0),(1,0)),((1,1),(1,0),(0,0),(0,-1)),((1,-1),(0,-1),(0,0),(-1,0))) # ㄹ
p4 = (((-1,1),(-1,0),(0,0),(0,-1)),((1,1),(0,1),(0,0),(-1,0)),((1,-1),(1,0),(0,0),(0,1)),((-1,-1),(0,-1),(0,0),(1,0)))# 대칭 ㄹ
p5 = (((-1,0),(0,-1),(0,0),(0,1)),((-1,0),(0,1),(0,0),(1,0)),((0,1),(1,0),(0,0),(0,-1)),((1,0),(0,-1),(0,0),(-1,0))) # ㅗ
p6 = (((-1,-1),(0,-1),(0,0),(0,1)),((-1,1),(-1,0),(0,0),(1,0)),((1,1),(0,1),(0,0),(0,-1)),((1,-1),(1,0),(0,0),(-1,0))) # ㄴ
p7 = (((-1,1),(0,-1),(0,0),(0,1)),((1,1),(-1,0),(0,0),(1,0)),((1,-1),(0,1),(0,0),(0,-1)),((-1,-1),(1,0),(0,0),(-1,0))) # ㄱ
pieces = [p1,p2,p3,p4,p5,p6,p7]

def create_block():
    global pieces
    block_num = int(random.random()*7)
    if block_num == 7:
        block_num = 0
    r, c = 0,5
    return r, c, block_num, 0

board =[[' | ']+['   ' for _ in range(10)]+[' | ']]
board.extend([[' | ']+['   ' for _ in range(10)]+[' | '] for _ in range(18)])
board.append(['   ']+[' ━ ' for _ in range(10)]+['   '])

no_block = True
con_game = True
def over_sideline(abs_r,abs_c,b_n,r_n): # 양 옆 경계에 닿았는가 닿았다면 어디에 얼마나 넘게 닿았는지 알려주는 함수
    global board,pieces
    piece = pieces[b_n][r_n]
    over = 0
    for rel_r,rel_c in piece:
        r,c = rel_r+abs_r, rel_c+abs_c
        if c < 1:
            over = min(over, c - 1)
        if c > 10:
            over = max(over, c - 10)
        # 양 사이드 라인 다 닿는 경우는 없으므로 이렇게 해도 된다.
    return over

def over_endline(abs_r,abs_c,b_n,r_n):
    global board,pieces
    piece = pieces[b_n][r_n]
    over = 0
    for rel_r,rel_c in piece:
        r,c = rel_r+abs_r, rel_c+abs_c
        if r > 18:
            over = max(over, r-18)
    return over

def touch_blocks(abs_r,abs_c,b_n,r_n): # 쌓여진 블록들에 닿았는가 알려주는 함수
    global board,pieces
    piece = pieces[b_n][r_n]
    for rel_r,rel_c in piece:
        r,c = rel_r+abs_r, rel_c+abs_c
        if board[r][c] == ' * ':
            return True
    return False

def rotate(abs_r,abs_c,b_n,r_n): # 블록을 회전시켜주는 함수
    global board,pieces
    if b_n == 1:
        return abs_r,abs_c,r_n
    nxt_r_n = (r_n + 1)%4
    piece = pieces[b_n][nxt_r_n]
    for rel_r,rel_c in piece:
        r,c = rel_r+abs_r, rel_c+abs_c
        if over_sideline(r,c,b_n,nxt_r_n):
            return abs_r,abs_c - over_sideline(abs_r,abs_c,b_n,nxt_r_n),nxt_r_n
        if over_endline(r,c,b_n,nxt_r_n):
            return abs_r-over_endline(r,c,b_n,nxt_r_n),abs_c,nxt_r_n
        if touch_blocks(r,c,b_n,nxt_r_n):
            return abs_r,abs_c,r_n
    return abs_r,abs_c,nxt_r_n
    
def move(k,abs_r,abs_c,b_n,r_n): 
    # 블록을 병진 이동 시키는 함수, 나가지 않았는지 먼저 확인한후 다른 블럭과 충돌을 확인한다.
    # 인덱스 나가는걸 방지하려고
    global board,pieces
    if k == 75:
        if touch_blocks(abs_r,abs_c-1,b_n,r_n) or over_sideline(abs_r,abs_c-1,b_n,r_n) :
            return abs_r,abs_c
        return abs_r,abs_c-1
    if k == 77:
        if touch_blocks(abs_r,abs_c+1,b_n,r_n) or over_sideline(abs_r,abs_c+1,b_n,r_n):
            return abs_r, abs_c
        return abs_r,abs_c+1
    if k == 80:
        if touch_blocks(abs_r+1,abs_c,b_n,r_n) or over_endline(abs_r+1,abs_c,b_n,r_n):
            return abs_r,abs_c
        return abs_r+1,abs_c
    
def downable(abs_r,abs_c,b_n,r_n): # 밑으로 내려갈 수 있는지 반환
    if not touch_blocks(abs_r+1,abs_c,b_n,r_n) and not over_endline(abs_r+1,abs_c,b_n,r_n):
        return True

def game_display(): # 콘솔화면에 현재상황 띄우기
    global board      
    for i in range(20):
        for j in range(12):
            print(board[i][j],end='')
        print()
    return
        
def block_clear(abs_r,abs_c,b_n,r_n): # 보드에 그려진 블록 지워주기
    global board,pieces
    for rel_r,rel_c in pieces[b_n][r_n]:
        r,c = abs_r+rel_r,abs_c +rel_c
        if 0<=r<=19:
            board[r][c] = '   '
    return
        
def block_add(abs_r,abs_c,b_n,r_n): # 보드에 블록 그려주기
    global board,pieces
    for rel_r,rel_c in pieces[b_n][r_n]:      
        r,c = abs_r+rel_r,abs_c +rel_c
        if 0<=r<=19:
            board[r][c] = ' * '
    return

def line_clear(abs_r,abs_c,b_n,r_n): # 꽉찬 행 삭제
    global board,pieces
    clear_line = set()
    for rel_r,rel_c in pieces[b_n][r_n]:
        if board[abs_r+rel_r].count(' * ') == 10:
            clear_line.add(abs_r+rel_r)
    clear_line = list(clear_line)
    clear_line.sort()
    for line in clear_line:
        board[:line+1] = [[' | ']+['   ' for _ in range(10)]+[' | ']] + board[:line] 
    return
                  
touch_sail = 0
running = True
touch_endline = False
block = False
while running:
    if not block:
        row, col, block_n, rot_n = create_block()
        block = True
        touch_endline = False
    block_add(row,col,block_n,rot_n)
    os.system('cls')
    game_display()
    start_time = time.time()
    while not touch_endline:
        block_clear(row,col,block_n,rot_n)
        if not downable(row,col,block_n,rot_n):
            touch_endline = True
            block_add(row,col,block_n,rot_n)
            block = False
            line_clear(row,col,block_n,rot_n)
            os.system('cls')
            if not downable(row,col,block_n,rot_n):
                print()
            game_display()
            touch_sail = board[0].count(' * ')
            if touch_sail :
                block = False
                running = False
                break
            else:
                touch_endline = False
                block = False
                break
        else:
            if time.time()-start_time > 0.2:
                start_time = time.time()
                block_clear(row,col,block_n,rot_n)
                row,col = move(80,row,col,block_n,rot_n)
                block_add(row,col,block_n,rot_n)
                break
            elif msvcrt.kbhit():
                k = msvcrt.getch()
                if ord(k) in [72,75,77,80]:
                    if ord(k) == 72:       
                        block_clear(row,col,block_n,rot_n)
                        row, col, rot_n = rotate(row,col,block_n,rot_n)
                    else:
                        block_clear(row,col,block_n,rot_n)
                        row, col = move(ord(k),row, col, block_n, rot_n)
    os.system('cls')  
    game_display()