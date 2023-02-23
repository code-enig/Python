# 언젠가 초기상태로 돌아오지 않을까?
# 0초 초기상태 셋팅
# 1초 대기
# 2초 그 후 초기상태 폭탄 설치 구역 외에 모두 폭탄 설치 
# 3초 초기상태 폭탄 모두 폭발
# 4초 그 후 빈칸에 모두 폭탄 설치
# 5초 2초에 설치한 폭탄이 모두 폭발 이 때 3초에서 초기상태 폭탄의 폭발으로 
# 2초에 설치된 초기상태 폭탄을 제거할 수 있는 모든 폭탄을 제거 하였으므로
# 4초에 설치된 폭탄 중 초기 상태 폭탄과 초기 상태 폭탄과 초기상태 주변 폭탄이 남는다. -> 
# 1-1 만약 초기상태 폭탄 주변의 폭탄이 하나도 없다면 1초 대기 상태로 돌아간다.
# 1-2 아니라면 새로운 초기상태로 돌아간다.
# 1-3 근데 초기상태 폭탄이 모두 폭발할 때 보드 위의 모든 폭탄이 제거될 수도 있다. 
# 결국 언제 사이클이 형성 되는지 체크해야한다.
import sys
import copy
sys.stdin = open('input','r')
r, c, n = map(int, sys.stdin.readline().split())
board = [[] for _ in range(r)]
cycle = []
second = 0
cycle_start = 0
not_find_cycle = True
for i in range(r):
    tmp_str = sys.stdin.readline()
    for j in range(c):
        if tmp_str[j] == "O":
            board[i].append(3)
        else:
            board[i].append(-1)
cycle.append(copy.deepcopy(board))

while not_find_cycle:
    second += 1
    for j in range(r):
        for k in range(c):
            board[j][k] -= 1
    explosion_list = []
    for j in range(r):
        for k in range(c):
            if  board[j][k] == 0 : # 폭탄 터짐
                explosion_list.append((j,k))
    for bomb in explosion_list:
        j,k = bomb
        board[j][k] = 0
        if j+1 < r :
            board[j+1][k] = 0
        if j-1 >= 0:
            board[j-1][k] = 0
        if k+1 < c :
            board[j][k+1] = 0
        if k-1 >= 0:
            board[j][k-1] = 0
    if not second%2: # 봄버맨이 일을 한다.
        for j in range(r):
            for k in range(c):
                if board[j][k] <=0:
                    board[j][k] = 3

    for l,prev_board in enumerate(cycle): # 이전에 같은 상황이 있었는지 검색 한다.
        for row in range(r):
            flag = False
            for col in range(c):
                if prev_board[row][col] != board[row][col]:
                    flag = True
                    break
            if flag:
                break
        else:
            not_find_cycle = False
            cycle_start = l
    if not_find_cycle:
        cycle.append(copy.deepcopy(board)) # 찾지 못하면 케이스에 넣고 계속 한다.

status = cycle[(n-cycle_start)%(len(cycle)-cycle_start)+cycle_start] if n>len(cycle)-1 else cycle[n]
for line in status:
    for space in line:
        print('.' if space <= 0 else "O", end="")
    print()