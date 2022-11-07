#힙
import sys
import heapq
N, k = map(int,sys.stdin.readline().split())
levels = []
for _ in range(N):
    heapq.heappush(levels, int(sys.stdin.readline()))

min_lv = heapq.heappop(levels)
count = 0
while levels:
    nxt_lv = heapq.heappop(levels)
    count += 1
    required_lvs = (nxt_lv - min_lv)*count
    if k >  required_lvs:
        min_lv = nxt_lv  
        k -= required_lvs
    elif k == required_lvs:
        k = 0
        min_lv = nxt_lv
        break
    else:
        add_lv = k//count
        k = 0
        min_lv += add_lv
        break
if k > 0:
    min_lv += k//N
print(min_lv)