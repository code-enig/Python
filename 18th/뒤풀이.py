# 특정 값보다 작은 값중에 가장 큰 값이나 큰 값중 가장 작은 값 찾는 BS
# 넴모넴모 2020 과 같은 알고리즘
# S가 넘지 않는 선에서 최대치의 술을 모두에게 나눠준다. 그러다가 술이 부족해지면 S를 낮춘다. 그러다가 술이 남으면 S를 높인다.
# => 큰 값중 가장 작은 값을 찾는 알고리즘
import sys
sys.stdin = open('18th\\input','r')
input = sys.stdin.readline

N,T = map(int, input().split())

max_l, tot_l, max_r, tot_r = 0, 0, 0, 0
s = 0
alcohol= [[],[]]
for _ in range(N):
    mn, mx = map(int, input().split())
    tot_l += mn
    tot_r += mx
    max_l= max(max_l, mn)
    max_r = max(max_r, mx)
    alcohol[0].append(mn)
    alcohol[1].append(mx)

if tot_l > T or tot_r < T:
    print(-1)
else:
    st, ed = max_l, max_r
    while st <= ed:
        mid = (st+ed)//2
        alcohol_sum = 0
        for i in range(N):
            alcohol_sum += alcohol[1][i] if alcohol[1][i] <= mid else mid
        if alcohol_sum >= T:
            ed = mid - 1
        else:
            st = mid + 1
    print(ed+1)