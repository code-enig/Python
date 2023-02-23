# BFS + DP
# 도시 N 개 도시간 경로의 갯수 ->N^2 ~40,000
from collections import deque
from collections import defaultdict
from sys import stdin
stdin = open("Python\\input",'r')
n = int(stdin.readline())
m = int(stdin.readline())

linked_cities_dict = defaultdict(set)
for i in range(n):
    linked_cities_dict[i].add(i)
    link_status = list(map(int, stdin.readline().split()))
    for j in range(n):
        if link_status[j]:
            linked_cities_dict[i].add(j)
            linked_cities_dict[j].add(i)

visited = [False for _ in range(n)]
  
q = deque()
q.append([0,linked_cities_dict[0]]) # 도시 번호와 도시에 연결된 도시들 set을 넣고
visited[0] = True
while q:
    city, linked_cities = q.popleft()
    for nxt_city in linked_cities:
        if not visited[nxt_city]:
            q.append([nxt_city,linked_cities_dict[nxt_city]]) # 큐에 넣고
            visited[nxt_city] = True
        linked_cities_dict[nxt_city] |= linked_cities # 서로 연결한다. 

def n_change(x):
    return int(x)-1
tour_plan = list(map(n_change,stdin.readline().split()))

start_city = tour_plan[0]
tour_plan = set(tour_plan)
if tour_plan-linked_cities_dict[start_city]:
    print("NO")
else:
    print("YES")