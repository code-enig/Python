# 누적합 같음?
import sys
sys.stdin = open('input','r')
n,h = map(int, sys.stdin.readline().split())

prefix1 = [0 for _ in range(h)]
prefix2 = [0 for _ in range(h)]

for i in range(n):
    obs = int(sys.stdin.readline())
    if i%2:
        prefix1[0] += 1
        prefix1[obs] -=1
    else:
        prefix2[-1] += 1
        prefix2[-1-obs] -= 1
        
for j in range(1,h):
    prefix1[j] += prefix1[j-1]
    prefix2[-1-j] += prefix2[-j]
    
total_prefix = [prefix1[k] + prefix2[k] for k in range(h)]
n = min(total_prefix)    
print(n, total_prefix.count(n))