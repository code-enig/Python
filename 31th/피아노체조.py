import sys
sys.stdin = open('input','r')
n = int(sys.stdin.readline())
difficulties = list(map(int,sys.stdin.readline().split()))
q = int(sys.stdin.readline())

n_miss = [0 for _ in range(n)]
for i in range(1,n):
    n_miss[i] = n_miss[i-1] + (1 if difficulties[i-1] > difficulties[i] else 0) # 그 곡을 치기 전 까지 발생한 실수 갯수를 담는다.
for _ in range(q):
    x,y = map(int, sys.stdin.readline().split())
    print(n_miss[y-1] - n_miss[x-1])        