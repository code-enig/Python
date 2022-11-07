import sys
import heapq
sys.stdin = open('22th\input','r')
N = int(sys.stdin.readline().strip())
# 수업 시작시간을 기준으로 하는 최소힙
class_q = []
for _ in range(N):
    heapq.heappush(class_q, list(map(int, sys.stdin.readline().split())))
#수업 끝나는 시간을 기준으로 하는 최소힙
room_q = [0]
while class_q:
    start = class_q[0][0]
    first_end = room_q[0]
    if start >= first_end: # 시작 시간이 가장 빨리 수업이 끝나는 교실의 끝나는 시간보다 늦다면
        # 가장 수업이 빨리 끝나는 교실의 수업이 끝나는 시간을 지금 수업의 끝나는시간으로 갱신한다.
        heapq.heappop(room_q) 
        heapq.heappush(room_q, heapq.heappop(class_q)[1])
    else:
        #아니라면 방을 하나 늘려야한다.      
        heapq.heappush(room_q, heapq.heappop(class_q)[1])

print(len(room_q))