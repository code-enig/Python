# 등대 n개, 뱃길 n-1개 존재, 모든 등대 이동 가능-> 사이클이 존재하지 않는 그래프-> 트리 구조
# DFS
import sys
sys.setrecursionlimit(100000)
from collections import defaultdict
def solution(n, lighthouse):
    global answer
    turn_on = [False for _ in range(n+1)]
    answer = 0
    connect = defaultdict(list)
    for a,b in lighthouse:
        connect[a].append(b)
        connect[b].append(a)

    def dfs(l,p):
        global answer
        condition = False
        if l!=1 and len(connect[l]) == 1 and not turn_on[p]:
            turn_on[p] = True
            answer += 1 # 리프 노드가 아닌 리프 노드 앞 노드를 켜는것
            return 
        for nxt in connect[l]:
            if nxt != p:
                dfs(nxt,l)
                if not turn_on[nxt]:
                    condition = True
        if not turn_on[l] and condition:
            turn_on[l] = True
            answer += 1
    dfs(1,0)        
    return answer

n, lighthouse = 12,[[1,2],[2,3],[3,4],[4,5],[4,6],[5,7],[5,8],[6,9],[6,10],[7,11],[8,12]]
print(solution(n,lighthouse))