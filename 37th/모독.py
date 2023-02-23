# 한명이라도 생긴다면 -> 0이 되는 값이 하나라도 존재한다면
# 명예는 감소 뿐이 못시키므로, 한 명예 그룹에서 다른 명예 그룹까지 계단을 만들어줘야 한다.
import sys
from collections import deque
sys.stdin = open('input','r')
n = int(sys.stdin.readline())
mps = []
for _ in range(n):
    mps.append(int(sys.stdin.readline()))

mps.sort()
honor_stairs = [0 for _ in range(mps[-1]+1)]
honor_group = deque(sorted(list(set(mps)))) # 명예 그룹
for honor in mps:
    honor_stairs[honor] += 1 # 명예 그룹의 국회의원 숫자

hackers = 0
step = 1
while honor_group:
    if not honor_stairs[step]:
        while step >= honor_group[0]:
            honor_group.popleft()
        if honor_stairs[honor_group[0]] > honor_group[0]-step: # 필요한 계단 숫자
            honor_stairs[honor_group[0]] -= honor_group[0]-step
            hackers += (honor_group[0]-step)*(honor_group[0]-step+1)//2
            step = honor_group.popleft()+1
        else:
            hackers += (honor_group[0]-step)*(honor_group[0]-step+1)//2
            step += honor_stairs[honor_group[0]]
            honor_stairs[honor_group[0]] = 0       
            hackers -= (honor_group[0]-step)*(honor_group[0]-step+1)//2
            honor_group.popleft() # 더 이상 존재하지 않는 명예 그룹이므로 삭제
    else:
        step = honor_group.popleft()+1

print(hackers)