# BFS
import sys
from collections import deque
sys.stdin = open("Python\\input",'r')
k = int(sys.stdin.readline())
w,h = map(int, sys.stdin.readline().split())
INF = float('inf')

def solution():
    visited =[[[True]*(k+1) for _ in range(w+4)] for _ in range(2)]
    for _ in range(h):
        inform = list(sys.stdin.readline().split())
        tmp = [[True]*(k+1)]*2
        tmp.extend( [[True]*(k+1) if int(inform[i]) else [False]*(k+1) for i in  range(w)])
        tmp.extend([[True]*(k+1)]*2)
        visited.append(tmp)
    visited.extend([[[True]*(k+1) for _ in range(w+4)] for _ in range(2)])
    m_steps = ((1,0),(0,1),(0,-1),(-1,0))
    h_steps = ((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))

    count = 0
    if h == 2 and w == 2:
        print(0)
        sys.exit(0)
    q = deque()
    q.append((2,2,k,0))
    visited[2][2] = [True]*(k+1)
    while q:
        r,c,left_h,steps= q.popleft()
        if r == h+1 and c == w+1:
            print(steps)
            return
        if left_h:
            for m_step in m_steps:
                nxt_r = r + m_step[0]
                nxt_c = c + m_step[1]

                if not visited[nxt_r][nxt_c][left_h]:
                    q.append((nxt_r,nxt_c,left_h,steps+1))
                    visited[nxt_r][nxt_c][left_h] = True
                    
            for h_step in h_steps:
                nxt_r = r + h_step[0]
                nxt_c = c + h_step[1]

                if not visited[nxt_r][nxt_c][left_h-1]:
                    q.append((nxt_r,nxt_c,left_h-1,steps+1))
                    visited[nxt_r][nxt_c][left_h-1] = True
        else:
            for m_step in m_steps:
                nxt_r = r + m_step[0]
                nxt_c = c + m_step[1]
                
                if not visited[nxt_r][nxt_c][0]:
                    q.append((nxt_r,nxt_c,0,steps+1))
                    visited[nxt_r][nxt_c][0] = True
        count += 1 
    print(-1)
    return
solution()