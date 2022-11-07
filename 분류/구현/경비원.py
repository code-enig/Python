# 4*4 = 16가지 케이스 다 나눠서

import sys

sys.stdin = open('17th\\input', 'r')
input = sys.stdin.readline
global width, height
width, height = map(int, input().split())
N = int(input())
shops = tuple(tuple(map(int, input().split())) for _ in range(N))
dg = tuple(map(int, input().split()))

min_dist = 0
for i in range(N):
    if dg[0] == 1:
        if shops[i][0] == 2:
            min_dist += min(shops[i][1] + dg[1], 2*width -shops[i][1]-dg[1]) + height
        elif shops[i][0] == 3:
            min_dist += shops[i][1] + dg[1]
        elif shops[i][0] == 4:
            min_dist += width - dg[1] + shops[i][1]
        else:
            min_dist += abs(shops[i][1] - dg[1])
    if dg[0] == 3:
        if shops[i][0] == 4:
            min_dist += min(shops[i][1] + dg[1], 2*height -shops[i][1]-dg[1]) + width
        elif shops[i][0] == 1:
            min_dist += dg[1] + shops[i][1]
        elif shops[i][0] == 2:
            min_dist += height - dg[1] + shops[i][1]
        else:
            min_dist += abs(shops[i][1] - dg[1])
    if dg[0] == 2:
        if shops[i][0] == 3:
            min_dist += height + dg[1] - shops[i][1]
        elif shops[i][0] == 4:
            min_dist += width + height - dg[1] - shops[i][1]
        elif shops[i][0] == 1:
            min_dist += min(shops[i][1] + dg[1], 2*width -shops[i][1]-dg[1]) + height
        else:
            min_dist += abs(shops[i][1] - dg[1])
    if dg[0] == 4:
        if shops[i][0] == 1:
            min_dist += width + dg[1] - shops[i][1]
        elif shops[i][0] == 2:
            min_dist += width+ height - dg[1] - shops[i][1]
        elif shops[i][0] == 3:
            min_dist += min(shops[i][1] + dg[1], 2*height -shops[i][1]-dg[1]) + width
        else:
            min_dist += abs(shops[i][1] - dg[1])

print(min_dist)
    