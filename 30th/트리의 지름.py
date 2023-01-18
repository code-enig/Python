# 임의 노드를 루트 노드로 정한다-> 그 노드로 부터 리프 노드를 찾는다. -> 
# 리프노드들로 부터 부모노드로 돌아가면서 트리의 지름과, 가장 긴 반지름(?)을 반환한다. -> 
# 임의의 노드까지 도달 하였을 때 가중치가 가장 큰 노드 두개를 연결한다.
# 수정 => 루트 노드가 주어진다.
import sys
sys.setrecursionlimit(100000)
from collections import defaultdict
sys.stdin = open('input','r')
n = int(sys.stdin.readline())
global nodes
nodes = defaultdict(list)
for _ in range(n-1):
    p_n, c_n, w = map(int,sys.stdin.readline().split())
    nodes[p_n].append([c_n,w])


def solution(p_n):
    global nodes
    max_d = 0
    mr, smr = 0, 0 # 그 노드에서 가장 긴 반지름과 두번 째로 긴반지름
    if not nodes[p_n]:
        return 0, 0
    for c_n,w in nodes[p_n]:
        r, d = solution(c_n)
        if r+w>mr:
            smr = mr
            mr = r+w
        elif r+w > smr:
            smr = r+w
        max_d = max(max_d,d,mr+smr)  
        
    return mr, max_d

print(solution(1)[1])