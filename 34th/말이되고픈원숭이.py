# BFS, 같은 횟수만큼 움직였을때 같은 위치에 도달했다면, 말 움직임이 적을 수록 유리하다.
import sys
from collections import deque
sys.stdin = open("Python\\input",'r')
k = int(sys.stdin.readline())
w,h = map(int, sys.stdin.readline().split())
def my_conv(x):
    ret =[-1]*2
    for ob in x:
        if ob == '1':
            ret.append(-1)
        else:
            ret.append(0)
    ret.extend([-1]*2)
    return ret

def solution():
    visited =[[-1 for _ in range(w+4)] for _ in range(2)]
    visited.extend([my_conv(sys.stdin.readline().split()) for _ in range(h)])
    visited.extend([[-1 for _ in range(w+4)] for _ in range(2)])
    m_steps = ((1,0),(0,1),(0,-1),(-1,0))
    h_steps = ((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))

    count = 0 # 몇번쨰 움직임인가
    q = deque([])
    q.append((2,2,1)) # 편의를 위해 1을 기본값으로 하자
    visited[2][2] = -1
    while q:
        for _ in range(len(q)):
            r,c,used_h= q.popleft()
            if r == h+1 and c == w+1:
                print(count)
                exit(0)
            if used_h < k + 1:             
                for h_step in h_steps:
                    nxt_r = r + h_step[0]
                    nxt_c = c + h_step[1]
                    if used_h + 1 < visited[nxt_r][nxt_c] or not visited[nxt_r][nxt_c]:
                        visited[nxt_r][nxt_c] = used_h + 1 
                        q.append((nxt_r,nxt_c,used_h + 1))
            for m_step in m_steps:
                nxt_r = r + m_step[0]
                nxt_c = c + m_step[1]
                if used_h < visited[nxt_r][nxt_c] or not visited[nxt_r][nxt_c]:
                    visited[nxt_r][nxt_c] = used_h
                    q.append((nxt_r,nxt_c,used_h))
        count += 1

    print(-1)
    return
solution()