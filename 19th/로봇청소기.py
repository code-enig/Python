import sys
sys.stdin = open('19th\\input','r')
input = sys.stdin.readline
N, M = map(int, input().split())
pr,pc,d_num = list(map(int, input().split()))
hall = [list(map(int, input().split())) for _ in range(N)]

dx = (0,1,0,-1)
dy = (-1,0,1,0)
power = True
check = 0
count = 0
while power:
    if not hall[pr][pc]: # 현재 위치를 청소한다.
        hall[pr][pc] = 2
        count += 1
    nxt_d_num = (d_num-1)%4 # 왼쪽 방향
    # 한 칸 전진
    nxt_pr = pr + dy[nxt_d_num]
    nxt_pc = pc + dx[nxt_d_num]
    if hall[nxt_pr][nxt_pc]: # 청소할 공간이 없다면
        d = nxt_d_num
        check += 1 # 사방중 한방향을 체크 하였음
    else:                   # 청소할 공간이 존재한다면
        d = nxt_d_num
        pr = nxt_pr
        pc = nxt_pc
        check = 0
        continue
    if check >= 4: # 사방이 막혔다면
        # 후진한다.
        pr = pr - dy[d_num]
        pc = pc - dx[d_num]
        if hall[pr][pc] == 1:
            power = False
        else:
            check = 0   
print(count)   