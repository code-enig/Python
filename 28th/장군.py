# BFS인것 같다
import sys
from collections import deque
sys.stdin = open('Python\\input','r')
r,c = list(map(int,sys.stdin.readline().split()))
start = (r+3,c+3)
r,c = list(map(int,sys.stdin.readline().split()))
end = (r+3,c+3)
visited = [[True for i in range(15)] for i in range(3)]
visited.extend([[True,True,True]+[False for i in range(9)]+[True,True,True] for _ in range(10)])
visited.extend([[True for i in range(15)] for i in range(3)])
visited[end[0]][end[1]] = True
# 1로 감싸서 체크 쉽게
st = ((1,0),(-1,0),(0,1),(0,-1))
di = (((1,1),(2,2)),((1,-1),(2,-2)),((-1,1),(-2,2)),((-1,-1),(-2,-2)))
comb = ((0,1),(2,3),(0,2),(1,3))
class LoopBreak(Exception):
    pass
min_number = -1
elepent_position = deque([])
visited[start[0]][start[1]] = True
elepent_position.append((start,0))
try:
    i = 1
    while elepent_position:
        (position_r,position_c), num = elepent_position.popleft()
        for s in range(4):
            nxt_r,nxt_c = position_r + st[s][0], position_c + st[s][1]
            if nxt_r != end[0] or nxt_c != end[1]: # 기물이 있으면 지나갈 수 없다.
                for c in comb[s]: # 그 방향으로 움직였을 떄 움직일수 있는 대각 방향의 종류
                    for i,d in enumerate(di[c]): # 대각 방향마다 
                        nxt_r,nxt_c = position_r + st[s][0] + d[0], position_c + st[s][1] + d[1]
                        if nxt_r == end[0] and nxt_c == end[1]: # 기물이 있으면 지나갈 수 없다.
                            if i == 1:
                                min_number = num + 1
                                raise LoopBreak()
                            break
                    else:
                        if not visited[nxt_r][nxt_c]:
                            visited[nxt_r][nxt_c] = True
                            elepent_position.append(((nxt_r,nxt_c),num+1))
except LoopBreak:
    pass
print(min_number)