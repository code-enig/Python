import sys
from collections import defaultdict
sys.stdin = open('input','r')
n,g,k = map(int,sys.stdin.readline().split())

not_important_ingredients = defaultdict(list) #중요하지 않은 재료 받을 해시테이블
important_ingredients = defaultdict(int) #중요한 재료 받을 해시테이블
# 원래는 일자별로 세균수 초깃값을 받으려고 헀는데 날짜 범위가 10^9 까지라서 배열 크기가 너무 크고 빈공간이 많으니까 해쉬 테이블로 바꿈
ini_germs = 0 # 초기 세균수
max_l = 0 # 가장 긴 유통기한
for _ in range(n):
    s,l,o = map(int,sys.stdin.readline().split())
    if o:
        not_important_ingredients[l].append(s) # 중요하지 않은 재료는 유통기한이 같은 날짜로 재료를 묶어서 초기 세균수를 리스트로 만듭
    else:
        important_ingredients[l] += s # 중요한 재료는 어차피 못빼니까 그냥 죄다 세균수를 합침
    ini_germs += s
    max_l = max(max_l,l)

l,r = 1, max_l + g
while l<=r:  # 2진 탐색//파라매트릭서치부분
    germs = ini_germs
    m = (l+r)//2
    removable_germs =[]
    for (date, factor) in important_ingredients.items():
        if m > date:
            germs += factor*(m-date-1) #문제에 주어진 공식에 따라 그 일자의 세균수를 구해서 더해준다.
    for (date, _list) in not_important_ingredients.items():
        if m > date:
            for s in _list:
                germs += s*(m-date-1) #문제에 주어진 공식에 따라 그 일자의 세균수를 구한다.
                removable_germs.append((s*(m-date))) # 그 중 제거할 수 있는 재료의 세균수를 따로 리스트로 뽑는다.
        else:
            for s in _list:
                removable_germs.append(s) # 유동기한이 지나지 않았더라도, 원래 세균수가 많아서 제거하는게 유리한 경우가 있다.
    removable_germs.sort()
    germs -= 0 if k == 0 else (sum(removable_germs[-k:]) if len(removable_germs)>=k else sum(removable_germs)) # K개의 재료를 제거한 뒤 세균수
    if germs<=g: # 이진탐색
        l = m+1
    else:
        r = m-1

print(r)