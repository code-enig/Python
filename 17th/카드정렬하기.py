# 최대한 큰 카드 덩이를 적게 합쳐야 한다. 최소힙 사용
import sys
import heapq

input = sys.stdin.readline
N = int(input())
answer = 0

deck_list = list(int(input()) for _ in range(N))
heapq.heapify(deck_list)

while len(deck_list) > 1:
    merged_deck = heapq.heappop(deck_list) + heapq.heappop(deck_list)
    answer += merged_deck
    heapq.heappush(deck_list, merged_deck)

print(answer)