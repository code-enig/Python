#64C3 ~40,000 완전 탐색 가능 + BFS
import sys
sys.stdin = open('Python\input','r')
N,M = map(int, sys.stdin.readline().split())

lab = [[1]+[1 for _ in range(M)] +[1]]
for _ in range(N):
    lab.append([1] + list(map(int,sys.stdin.readline().split())) +[1])
lab.append([1]+[1 for _ in range(M)] +[1])

def choose_wall(start_r,start_c,n):
    n == n - 1
    for r in lab[start_r:]:
        if r == start_r:
            for c in r[start_c+1:]: # 처음에 벽으로 둘러 쌓았으므로 인덱스 에러 걱정 없음
                if lab[r][c] == 0:
                    if n == 0:
                        return r, c
                    return r, c, choose_wall(r, c,n-1)
        else:
            for c in r:
                if lab[r][c] == 0:
                    if n == 0:
                        return r, c
                    return r, c, choose_wall(r, c,n-1)
print(choose_wall(0,-1,3))

