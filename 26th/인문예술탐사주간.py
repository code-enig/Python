# 10^5*10^5>>10^9
import sys
import bisect
sys.stdin = open('Python\\26th\\input','r')
N,Q = map(int,sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

trees.sort()
c_sum = []
c_sum.append(trees[0])
for i in range(1,N):
    c_sum.append(c_sum[-1]+trees[i])

inputs = sys.stdin.readlines()
for x in inputs:
    x = int(x)
    if x >= trees[-1]:
        print(x*N - c_sum[-1])
        continue
    if x <= trees[0]:
        print(c_sum[-1] - x*N)
        continue
    # 나무 범위 바깥 배제
    idx = bisect.bisect_left(trees, x)
    if trees[idx] == x:
        print(x*(idx)-c_sum[idx-1] + (c_sum[-1]-c_sum[idx])-x*(N-idx-1))
    else:
        print(x*(idx)-c_sum[idx-1] + (c_sum[-1]-c_sum[idx-1])-x*(N-idx))
