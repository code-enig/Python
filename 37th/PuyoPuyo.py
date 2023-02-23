# RGBPY 방문 체크 => set()
import sys
from collections import deque
sys.stdin = open('input','r')
field = []
for _ in range(12):
    tmp = sys.stdin.readline().rstrip()
    line = []
    for ch in tmp:
        line.append(ch)
    field.append(line)
dr = (1,0,-1,0)
dc = (0,1,0,-1)

def more_than_three(color,row,col): # 특정 색이 4개 이상 모인 그룹이 있는지 알려주는 함수, 그리고 있다면 그 그룹들을 모두 터뜨린다.
    q= deque([])
    q.append([color,row,col])
    group = []
    group.append([row,col])
    visited[row][col].add(color)
    while q:
        cr, r, c, = q.popleft()
        for i in range(4):
            nxt_r, nxt_c = r+dr[i], c+dc[i]
            if 0 <= nxt_r < 12 and 0 <= nxt_c < 6 and cr == field[nxt_r][nxt_c] and cr not in visited[nxt_r][nxt_c]:
                q.append([cr,nxt_r,nxt_c])
                visited[nxt_r][nxt_c].add(cr)
                group.append([nxt_r,nxt_c])
    if len(group) >= 4:
        for r,c in group:
            field[r][c] = '.'
        return True
    return False

def gravity(): # 뿌요들을 모두 아래로 떨어뜨리는 함수
    for j in range(6):
        empty = -1
        find = False
        up_puyo = []
        for i in range(11,-1,-1):
            if not find and field[i][j] == '.':
                empty = i
                find = True
            if find and field[i][j] != '.':
                up_puyo.append(field[i][j])
                field[i][j] = '.'
        if up_puyo:
            for k,puyo in enumerate(up_puyo):
                field[empty-k][j] = puyo

count = 0
while True:
    new_chain = False
    visited = [[set() for _ in range(6)] for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j] == '.':
                continue
            if more_than_three(field[i][j],i,j):
                new_chain = True
    gravity()
    if not new_chain:
        break
    count += 1
print(count)