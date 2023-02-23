# dfs,bfs-> 어차피 한 역에 내리면 그 라인은 모두 방문 가능
# 그 모든 역중에 환승역에서 갈수잇는 라인을 모두 찾는다.
# 모두 찾은 라인에 대해서 위 내용 반복하면서 목적지 찾기
# 없으면 -1 
# 역번호 범위는 2^32-1 로 매우크지만 갯수는 < 100 이므로 set 사용
# 양방향
import sys
from collections import defaultdict
sys.stdin = open('input','r')
n = int(sys.stdin.readline())
sts_by_line = [set() for _ in range(n)] # 라인마다 역 
lines_by_st = defaultdict(set) # 역 마다 라인
visited = [False for _ in range(n)]
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(1,tmp[0]+1):
        sts_by_line[i].add(tmp[j])
        lines_by_st[tmp[j]].add(i)
dt = int(sys.stdin.readline())

def solution(start_lines,count=0):
    nxt_start_lines = set()
    for l in list(start_lines):
        for st in sts_by_line[l]:
            if st == dt:
                return count
            for nxt_l in lines_by_st[st]:
                if not visited[nxt_l]:
                    nxt_start_lines.add(nxt_l)
                    visited[nxt_l] = True
    if nxt_start_lines:
        return solution(nxt_start_lines,count+1)
    return -1

print(solution(lines_by_st[0]))