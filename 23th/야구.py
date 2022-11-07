import sys
from itertools import permutations
sys.stdin = open("23th\\input",'r')
input = sys.stdin.readline
N = int(input())


batting_orders_wo_n4 = list(permutations([i for i in range(1,9)]))
batting_orders = []
for o in batting_orders_wo_n4:
    batting_orders.append(list(o[:3])+[0]+list(o[3:]))

scores = [0 for _ in range(len(batting_orders_wo_n4))] # 타순에 따른 점수
abs = [0 for _ in range(len(batting_orders_wo_n4))] # 몇번 타순인지 알려주는 값
for _ in range(N):
    hits = list(map(int,input().split())) # 이닝 결과
    for i in range(len(batting_orders)):
        out_count = 0
        b1,b2,b3 = 0,0,0 # 루 주자 정보
        while out_count < 3: # 3아웃 전까지 이닝 진행
                if hits[batting_orders[i][abs[i]]] == 0:
                    out_count += 1
                elif hits[batting_orders[i][abs[i]]] == 1:
                    scores[i] += b3
                    b1,b2,b3 = 1,b1,b2
                elif hits[batting_orders[i][abs[i]]] == 2:
                    scores[i] += b2+b3
                    b1,b2,b3 = 0,1,b1
                elif hits[batting_orders[i][abs[i]]] == 3:
                    scores[i] += b1+b2+b3
                    b1,b2,b3 = [0,0,1]
                else:
                    scores[i] += b1+b2+b3+1
                    b1,b2,b3 = 0,0,0     
                abs[i] = (abs[i]+1)%9 # 반복되는 타순
print(max(scores))