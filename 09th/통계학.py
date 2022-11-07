import sys
from collections import defaultdict
import heapq

def countnumber(numbers):
    counter = defaultdict(int)
    for number in numbers:
        counter[number] += 1
    return counter

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
avg = int(round(sum(numbers)/len(numbers),0))
print(avg)
numbers.sort()
meadian = numbers[len(numbers)//2]
print(meadian)
counter = countnumber(numbers)
modeheap =[]
for k,v in counter.items():
    heapq.heappush(modeheap,(-v,k))
v, k  = heapq.heappop(modeheap)
if modeheap:
    tmp_v, tmp_k = heapq.heappop(modeheap)
    if tmp_v == v :
        print(tmp_k)
    else:
        print(k)
else:
    print(k)
ran = max(numbers)-min(numbers)
print(ran)
