# 10억-> 8억비트 -> 100MB->메모리초과
# 힙-> 시간초과
import sys
import heapq
sys.stdin = open('Python\\26th\\input','r')
N = int(sys.stdin.readline())
l_start = [0]*N
l_end = [0]*N
for i in range(N):
    start, end = map(int,sys.stdin.readline().split())
    l_start[i] = start
    l_end[i] = end
l_start.sort()
l_end.sort()

max_overlap = 0
now_overlap = 0
j = 0
for i in range(N):
    while j < N:
        if l_start[i] < l_end[j]:
            now_overlap += 1
            break
        elif l_start[i] > l_end[j]:
            max_overlap = max(max_overlap,now_overlap)
            now_overlap -= 1
            j += 1
        else:
            j += 1
            break
max_overlap = max(max_overlap,now_overlap) # 마지막 비교
print(max_overlap)