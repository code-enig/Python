import sys
import heapq
from collections import defaultdict
sys.stdin = open('Python\\input','r')
i_value = float('inf')
n,m,x,y = map(int,sys.stdin.readline().split())
naver = defaultdict(dict)
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    naver[a].update({b:c})
    naver[b].update({a:c})

def make_distance_list():
    min_value_heap = []
    distance = [i_value for _ in range(n)]
    distance[y] = 0
    heapq.heappush(min_value_heap, [0,y])
    while min_value_heap:
        acc_d,now = heapq.heappop(min_value_heap)
        if distance[now] < acc_d: # 한번 힙에 넣었었는데 이후에 갱신되었다면 무시
            continue
        for nxt,dist in naver[now].items():
            if acc_d + dist < distance[nxt]:
                distance[nxt] = acc_d + dist
                heapq.heappush(min_value_heap,[distance[nxt],nxt])
    return distance

def solution(distance):
    day = 0
    ix = 1 # 오늘 첫 방문해야하는 집 인덱스
    distance.sort()
    while True:
        d = 0 # 오늘 하루 누적 이동거리
        start = ix # ix 에서 출발
        while ix < len(distance) :
            if d + 2*distance[ix] <= x:
                d += 2*distance[ix]
                ix+= 1
            else:
                break
        if start == ix: # 아무곳에도 도달하지 못하였다면
            break
        day += 1
    if ix != n:
        print(-1)
    else:
        print(day)
    return 

solution(make_distance_list())