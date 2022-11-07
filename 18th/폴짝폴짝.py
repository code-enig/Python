# BFS? DFS? BFS 가 뛰는 숫자 세기 매우 편함
# 자기가 몇번째 노드인지 기억하고 있다가 자기 다음 노드로 마지막 징검다리가 올 수 잇으면 자기 번호를 반환하고 종료
from collections import deque
import sys
sys.stdin = open('18th\\input','r')
input = sys.stdin.readline

N = int(input())
bridge = list(map(int, input().split()))
a,b = map(int, input().split())

n = -1
q = deque([])
q.append((0,a)) # 0번 점프해서 a 위치에 있다.
if a == b:
    print(0)
else:
    while q:
        start = q.popleft()
        inv = bridge[start[1]-1]
        if not abs(b-start[1])%inv: # 출발지에서 목적지까지 한번에 갈 수 있으면
            n = start[0] + 1
            break
        for point in range(start[1]+inv,N, inv):
            q.append((start[0]+1,point))
        for point in range(start[1]-inv,-1, -inv):
            q.append((start[0]+1,point))
    print(n)