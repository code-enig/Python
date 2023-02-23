# 구성이 같은데 순서만 다른 우주의 쌍은 한번만 센다.
# 순서를 매기고 값에 따라 정렬했는데 매긴 순서의 순서 같다면 만족한다.
# {값:순서}를 값에 따라 정렬-> 이때 순서의 순서가 같다면 만족
# 딕셔너리를 활용해서 정렬해본다.
# 그것을 정렬하고 낮은 값부터 순서를 매긴 딕셔너리를 만든다. ex(1:0, 3:1, 5:2)
# 부피 리스트에 딕셔너리[값리스트 값]를 대입한다.
# 이렇게 하면 부피 리스트에는 행성들을 부피순으로 나열했을 때 그 행성의 순서가 들어가게 된다.
# 같은 부피의 행성은 같은 순서를 가지게 되면서...
from sys import stdin
from collections import defaultdict
m,n = map(int,stdin.readline().split())
orderverse = defaultdict(int)
for _ in range(m):
    tmp = list(map(int, stdin.readline().split()))
    tmp_list = sorted(list(set(tmp)))
    order_dict = {tmp_list[i]:i for i in range(len(tmp_list))}
    dict_key = str([order_dict[i] for i in tmp]) 
    # 딕셔너리를 또 다른 딕셔너리의 키로 쓰기 위한 트릭
    # 여기서 서로 다른 딕셔너리란 서로 균등하지 않은 우주들의 딕셔너리이기 때문에 
    # 위와 같이 하면 서로 다른 우주들은 서로다른 딕셔너리 키값을 가질수 있게 된다. 
    orderverse[dict_key] += 1
count = 0
for k,v in orderverse.items():
    count += v*(v-1)//2 # 다각형의 꼭지점의 자신 빼고 다른 점들과 있는 선분의 갯수
            
print(count)

orderverse.append([order_dict[tmp[i]] for i in range(len(tmp))])

count = 0
for i in range(len(orderverse)-1):
    for j in range(i+1,len(orderverse)):
        if orderverse[i] == orderverse[j]:
            count += 1