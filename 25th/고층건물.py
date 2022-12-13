# N = 50*49 완전 탐색 가능
# 가까운 순으로 각 건물까지 기울기를 구하고 가까운 건물보다 기울기가 크면 보이는 건물

import sys
sys.stdin = open('Python\\25th\\input','r')
input = sys.stdin.readline
N = int(input())
bds = list(map(int,input().split()))
max_num = 0
INF = float('inf')
for i in range(len(bds)):
    tan1, tan2, num = -INF,-INF, 0
    for j in range(i-1,-1,-1):
        tan = (bds[j]-bds[i])/(i-j)
        if tan>tan1:
            tan1 = tan
            num += 1
    for k in range(i+1,len(bds)):
        tan = (bds[k]-bds[i])/(k-i)
        if tan>tan2:
            tan2 = tan
            num += 1
    max_num = max(num,max_num)
print(max_num)