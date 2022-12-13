# 문자열을 쭉 읽으면서 N 종류로 읽을 수 있는 최대 문자열 길이를 계속 갱신한다.
import sys
import heapq
from collections import defaultdict
sys.stdin = open('Python\\26th\\input','r')
input = sys.stdin.readline
N = int(input())
index_heap = [] # 연속해서 등장하는 문자의 시작인덱스와 문자 종류를 담을 최소힙
type_count = defaultdict(int) # 현재 탐색중이 문자열에서 해당 문자가 시작된 횟수를 담을 dict
answer = 1
tmp_answer = 1
string = input()
types = set([string[0]])# 문자열에 등장하는 문자 종류
heapq.heappush(index_heap,(0,string[0]))
type_count[string[0]] += 1
for i in range(1,len(string)):
    if string[i] != string[i-1]:
        if string[i] not in types:
            if len(types) < N: 
                types.add(string[i])
                heapq.heappush(index_heap,(i,string[i]))
                type_count[string[i]] += 1
            else:
                answer = max(answer, i - index_heap[0][0])
                while True:
                    idx,a = heapq.heappop(index_heap)
                    type_count[a] -= 1
                    if type_count[a] == 0:
                        types.remove(a)
                        break
                heapq.heappush(index_heap,(i,string[i]))
                type_count[string[i]] += 1
                types.add(string[i])
                tmp_answer = i - index_heap[0][0] + 1
        else:
            heapq.heappush(index_heap,(i,string[i]))
            type_count[string[i]] += 1

answer = max(answer, i - index_heap[0][0])
print(answer)