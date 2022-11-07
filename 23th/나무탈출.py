# 성원이가 홀수번째 턴을 가져가므로, 홀수번째에 모든 말이 사라지면 성원이의 승리
# 따라서 루트노드에서 리프노드까지 모든 거리의 합이 홀수이면 성원이의 승리
import sys
from collections import defaultdict
sys.setrecursionlimit('500000')
sys.stdin = open('23th\\input','r')
input = sys.stdin.readline

def dfs(p,n,l): # p는 부모 노드 번호,n은 노드 번호, 루트에서 노드 n 까지 거리
    global total
    if n!= 1 and len(node_inf[n]) == 1: #연결된 노드가 하나뿐이면 리프 노드이다.(루트 노드에 바로 리프노드 하나만 달린경우 예외)
        total += l
        return
    for next in node_inf[n]:
        if next != p: # 트리구조이므로 앞만 보면 된다.
            dfs(n,next,l+1)
    return
total = 0
N = int(input())
node_inf = defaultdict(list)
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    node_inf[n1].append(n2)
    node_inf[n2].append(n1)
dfs(0,1,0)
print('Yes' if total%2 else 'No')