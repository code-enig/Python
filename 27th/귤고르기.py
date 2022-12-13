from collections import defaultdict
import heapq
def solution(k, tangerine):
    answer = 0
    number_size = defaultdict(int) # 크기별로 몇개인지 저장할 딕셔너리
    max_heap = [] # 개수를 인자로하여 저장할 최대힙
    for gyul in tangerine:
        number_size[gyul] += 1
    for size,number in number_size.items():
        heapq.heappush(max_heap,[-number,size])
    num_sum = 0
    while num_sum < k:
        number, size = heapq.heappop(max_heap) # 가장 많은 갯수를 가진 귤 크기가 하나 튀어나온다.
        num_sum -= number
        answer += 1 # 몇개의 귤 크기를 꺼냈는가
    return answer

k, tangerine = 2,[1, 1, 1, 1, 2, 2, 2, 3]
print(solution(k, tangerine))