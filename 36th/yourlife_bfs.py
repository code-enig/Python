# x<y 이므로 사이클은 생기지 않는다.
import sys
from collections import deque,defaultdict
sys.stdin = open('input','r')
n,m = map(int,sys.stdin.readline().split())
situatoin_inf = defaultdict(list)
visited = [False for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    situatoin_inf[x].append(y)

change = 0
visited[1] = True
q= deque([1])
while q:
    for _ in range(len(q)):     
        situation_now = q.popleft()
        for situation_nxt in situatoin_inf[situation_now]:
            min_situation = min(min_situation,situation_nxt)
            if situation_nxt == n:
                visited[situation_nxt] = True
                break
            if not visited[situation_nxt]:
                q.append(situation_nxt)
                visited[situation_nxt] = True
        if visited[n]:
            break
    change += 1
    if visited[n]:
        break 
       
print(change if visited[n] else -1)