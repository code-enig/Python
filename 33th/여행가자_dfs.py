# DFS + DP
# 도시 N 개 도시간 경로의 갯수 ->N^2 ~40,000
from sys import stdin
stdin = open("Python\\input",'r')
n = int(stdin.readline())
m = int(stdin.readline())
tour_board = [list(map(int,stdin.readline().split())) for _ in range(n)]


def n_change(x):
    return int(x)-1

def tour(origin, city):
    visited[city] = True
    for nxt_city in range(n):
        if not visited[nxt_city] and tour_board[nxt_city][city]:
            tour_board[origin][nxt_city] = 1
            tour_board[nxt_city][origin] = 1
            tour(origin, nxt_city)
    return

tour_plan = list(map(n_change,stdin.readline().split()))
start = tour_plan[0]

visited = [False for _ in range(n)]
tour_board[start][start] = 1
tour(start, start)

for city in tour_plan:
    if not tour_board[city][start]:
        print("NO")
        break
else:
    print("YES")