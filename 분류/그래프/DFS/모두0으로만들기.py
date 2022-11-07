# 지표면 위에 있는 흙덩이를 옮겨서 바다를 메운다고 생각(평탄화작업) 
# 한곳에서 흙을 퍼서 한칸씩 이동하여 옮긴다.
# 흙으로 다 메우면 끝이난다. 다 메울수 없다면 = -부분과 + 부분이 서로 같은 양이 아니다
# + 에 있는 것을 그냥 아무곳에 있는 -에 버리면된다. 방법은 여러가지가 있을 수 있으나, 한번에 옮기는양과 거리가 같기 때문에 어떻게 버려도 다시 퍼내지만 않으면 된다.
# 예를 들어 [-5 -1 1 2 3] 의 일직선을 생각해보면 1은 -1을 메꾸고 2 3은 -5에 버리면 된다(1 + 2*3 + 3*4= 19). 1을 -5 에 버리면 2 나 3을 -1에 버릴수 있지만 어차피 2 3은 
# 1을 거쳐가야하기 때문에 결과는 같다(2 + 2(2를 -1에 버림) + 3(2를 -5에 버림) + 3*4 = 19). 
# 또한 위와 같은 이유로 3에서 -1로 버리고 남은것을 -5 에 버리고 시작해도 결과는 19로 같다.
# 따라서 어떤 + 에서 시작하든 제일 가까운 -로 버리면 된다.
# 어디서 부터 시작해야하나? 루트 노드 기준으로 끝에서부터 퍼다 나르면 결국 루트 노드에서 다 만나서 사라질테니까 루트 노드에서 계속 해서 자식 노드로 탐색
# => DFS
import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict

def solution(a, edges):
    global graph
    global numbers
    numbers = a
    global visited
    visited = 0
    global answer
    answer = 0
    if sum(a) != 0:
        return -1
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    dfs(0)
    return answer

def dfs(parent):
    global answer
    global visited
    global graph
    global numbers
    carry = numbers[parent]
    last = True
    visited = visited|1<<parent
    for node in graph[parent]:
        if not(visited & 1<<node):
            carry += dfs(node)
            last = False
    if last:
        carry = numbers[parent]
    answer += abs(carry)
    return carry
a =[-5,0,2,1,2]
edges =	[[0,1],[3,4],[2,3],[0,3]]

print(solution(a,edges))