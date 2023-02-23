# DFS 시간복잡도 O(N+E)~20,000
from sys import setrecursionlimit
setrecursionlimit(20000)
def solution(maps):
    answer = []
    global stay_days,dr,dc,depth,width
    dr = (1,0,-1,0)
    dc = (0,1,0,-1)
    stay_days = []
    for line in maps:
        tmp = []
        for grid in line:
            if grid == 'X':
                tmp.append(0)
            else:
                tmp.append(int(grid))
        stay_days.append(tmp)
    depth = len(stay_days)
    width = len(stay_days[0])
    for r in range(depth):
        for c in range(width):
            if stay_days[r][c]:
                answer.append(dfs(r,c))
    answer.sort()
    if answer:
        return answer
    return [-1]
def dfs(r,c):
    global stay_days, dr, dc,depth,width
    count = stay_days[r][c]
    stay_days[r][c] = 0
    for i in range(4):
        nxt_r = r + dr[i]
        nxt_c = c + dc[i]
        if 0 <= nxt_r < depth and 0 <= nxt_c < width:
            if stay_days[nxt_r][nxt_c]:
                count += dfs(nxt_r,nxt_c)
    return count
                        

print(solution(["XXX","XXX","XXX"]))