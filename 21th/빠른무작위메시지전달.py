# 6!*2^6 = 46080 => 완전 탐색
import sys
from itertools import permutations
from itertools import product
input = sys.stdin.readline
g_order_list = list(permutations([i for i in range(6)]))
tt = [list(map(int,input().split())) for _ in range(12)]
in_g_order_list = list(product(((0,1),(1,0)), repeat=6))
INF = float('inf')
min_time = INF

for g in g_order_list:
    for in_g in in_g_order_list:
        time = 0
        for i in range(5):
            time += tt[g[i]*2+in_g[i][0]][g[i]*2+in_g[i][1]] + tt[g[i]*2+in_g[i][1]][g[i+1]*2+in_g[i+1][0]]
        time +=tt[g[5]*2+in_g[5][0]][g[5]*2+in_g[5][1]]
        min_time = min(time, min_time)
print(min_time)