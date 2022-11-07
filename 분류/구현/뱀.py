# 링크드리스트, 2차원 배열
from sys import stdin
from collections import deque
stdin = open('19th\\input','r')
input = stdin.readline

N = int(input())
K = int(input())
apples = [[0 for i in range(N)] for j in range(N)]
for _ in range(K):
    r,c = map(int, input().split())
    apples[r-1][c-1] = 1
L = int(input())
orders = [input().split() for _ in range(L)]
# 방향
dx = (1,0,-1,0)
dy = (0,1,0,-1)
d_num = 0
# 뱀
snake_board = [[0 for i in range(N)] for j in range(N)] # 뱀위 위치를 표현할 2차원 배열
snake_stack = deque([]) # 뱀의 연결된 순서를 저장할 링크드리스트
snake_board[0][0] = 2
snake_stack.append((0,0))
# 시작
seconds = 1
order_number = 0
order_length = len(orders)
while True:
    nxt_head_r, nxt_head_c = snake_stack[-1][0] + dy[d_num], snake_stack[-1][1] + dx[d_num]
    if 0 <= nxt_head_r <= N-1 and 0<= nxt_head_c <= N-1 and not snake_board[nxt_head_r][nxt_head_c]: # 벽 또는 자기자신의 몸과 부딪히지 않았다면
        snake_board[nxt_head_r][nxt_head_c] = 2
        snake_stack.append((nxt_head_r,nxt_head_c))
        if not apples[nxt_head_r][nxt_head_c]: # 사과가 없다면
            tail_r,tail_c = snake_stack.popleft()
            snake_board[tail_r][tail_c] = 0
        else:                                   # 사과가 있으면 먹는다.
            apples[nxt_head_r][nxt_head_c] = 0
    else:
        break
    if order_number < order_length and int(orders[order_number][0]) == seconds: # 명령이 남아있을 때까지, 지정한 시간이 되면 방향 전환
        d_num += 1 if orders[order_number][1] == 'D' else -1
        d_num = d_num%4
        order_number += 1
    seconds += 1
   
print(seconds)