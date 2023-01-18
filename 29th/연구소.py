#64C3 ~40,000 완전 탐색 가능 + BFS
import sys
from collections import deque
sys.stdin = open('input','r')
N,M = map(int, sys.stdin.readline().split())
global lab
lab = [[1]+[1 for _ in range(M)] +[1]]
for _ in range(N):
    lab.append([1] + list(map(int,sys.stdin.readline().split())) +[1])
lab.append([1]+[1 for _ in range(M)] +[1])

def choose_walls(n,walls = [[]]): # 벽 조합을 반환하는 함수
    global lab
    if not n :
        return walls
    chosen_walls = walls
    tmp_nxt_chosen_walls = []
    for wall in chosen_walls:
        if wall:
            start_r, start_c = wall[len(wall)-1]
            if wall[len(wall)-1][1] >= M+1: # 고른 벽이 있고 그 벽이 마지막 칼럼이라면
                start_r += 1 # 다음 행으로 간다.
                start_c = 1 # 열은 초기화
            else:
                start_c += 1 # 다음 열로 간다.
        else:
            start_r, start_c = 0, 0
        for r in range(start_r,N+1): # 골라진 벽 다음부터 고른다.
            if r == start_r:
                for c in range(start_c,M+1):
                    if lab[r][c] == 0:
                        tmp_nxt_chosen_walls.append(wall+[[r,c]])

            else:
                for c in range(1,M+1):
                    if lab[r][c] == 0:
                        tmp_nxt_chosen_walls.append(wall+[[r,c]])
    return choose_walls(n-1,tmp_nxt_chosen_walls)

def max_safe_zone(walls_list): # 안전 영역의 최댓값을 반환하는 함수
    global lab
    safe_zone_max = 0 
     # 벽설치를 시뮬레이션 해볼 연구소
    visited = [[-1 for _ in range(M+2)] for _ in range(N+2)]
    for i,walls in enumerate(walls_list):
        safe_zone = 0
        for wall in walls:
            visited[wall[0]][wall[1]] = i
        q = deque([])
        for r in range(1,N+1):
            for c in range(1,M+1):
                if lab[r][c] == 2:
                    q.append([r,c])
        while q:
            r,c = q.popleft()
            if not lab[r+1][c] and visited[r+1][c] != i: 
                q.append([r+1,c])
                visited[r+1][c] = i
            
            if not lab[r][c+1] and visited[r][c+1] != i: 
                q.append([r,c+1])
                visited[r][c+1] = i
                
            if not lab[r-1][c] and visited[r-1][c] != i: 
                q.append([r-1,c])
                visited[r-1][c] = i
            
            if not lab[r][c-1] and visited[r][c-1] != i: 
                q.append([r,c-1])
                visited[r][c-1] = i
                
        for r in range(1,N+1):
            for c in range(1,M+1):
                safe_zone += 1 if not lab[r][c] and visited[r][c] != i else 0
        safe_zone_max = max(safe_zone_max, safe_zone)
    
    return safe_zone_max

print(max_safe_zone(choose_walls(3)))     