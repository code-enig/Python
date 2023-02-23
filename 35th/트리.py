from sys import stdin
from collections import defaultdict
stdin = open('input','r')
n = int(stdin.readline())
node_inf = list(map(int, stdin.readline().split()))
n_child = [0 for _ in range(n)] # 자식 노드 숫자 인지 아닌지
n_leaves = [0 for _ in range(n)] # 자기 밑으로 리프 노드가 몇개인지
node = {} # 노드 정보
root = 0 # root node 번호
del_node = int(stdin.readline()) # 삭제할 노드 번호
for c,p in enumerate(node_inf):
    if p != -1:
        n_child[p] += 1
    else:
        root = c
    node[c] = p
    
def count_leaves(i):
    if i == root:
        return 
    if node[i] != del_node: # 삭제 된 노드에 도달하면 더 올라가기를 멈춰버린다.
        n_leaves[node[i]] += 1
        count_leaves(node[i])
    return

def solution():
    n_child[node[del_node]] -= 1 # 부모노드에서 자식 노드 숫자를 하나 줄임
    del node[del_node] # 노드 정보 삭제
    for i in range(n):
        if i != del_node and not n_child[i]: # 자식 노드가 없다면 리프 노드이므로
            count_leaves(i)
    if not n_child[root]: # 루트 노드 하나만 남으면
        print(1)
    else:
        print(n_leaves[root])
    return
solution()