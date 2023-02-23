# 제한 조건: 돈 k 를 다 쓸 것 , 모든 학생과 친구가 될것 2종류
# O(n)~1만,dfs
from collections import defaultdict
import sys
sys.setrecursionlimit(20000)
sys.stdin = open('Python\\input','r')
n,m,k = map(int, sys.stdin.readline().split())
freinds_relation = defaultdict(set) # 중복 제거하려 set 사용
freind_money = [0]
freind_money.extend(list(map(int, sys.stdin.readline().split())))
for _ in range(m):
    v,w = map(int, sys.stdin.readline().split())
    if v != w:
        freinds_relation[v].add(w)
        freinds_relation[w].add(v)

def dfs(s):
    min_money = freind_money[s]
    freind[s] = True
    for f_f in freinds_relation[s]:
        if not freind[f_f]:
            freind[f_f] = True
            min_money = min(dfs(f_f),min_money) # 연결된 친구 중에 가장적은 친구비를 찾는다.dfs
    return min_money

def solution():
    t_money = 0
    global freind
    freind = [False for _ in range(n+1)]
    for i in range(1,n+1):
        if not freind[i]:
            freind[i] = True
            t_money += dfs(i)
        if t_money > k:
            print("Oh no")
            break
    else:
        print(t_money)
    return

solution()