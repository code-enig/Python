import sys
sys.stdin = open('input' ,'r')
n,m = map(int, sys.stdin.readline().split())
dok = list(map(int,sys.stdin.readline().split()))

max_a = 0
a = 0
l= -1 
for r in range(n):
    a += dok[r]
    if a <=m:
        max_a = max(a, max_a)
    else:
        l += 1 # 반드시 움직여야하고 처음 출발은 -1 이므로 오류 방지
        a -= dok[l]
        while a > m and l < r:
            l += 1
            a -= dok[l]
        if a<=m : # l<r 때문에 탈출한 경우 대비
            max_a = max(a, max_a)
print(max_a)