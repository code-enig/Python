# 나머지
from sys import stdin
stdin = open('20th\\input','r')
input = stdin.readline
T = int(input())

for _ in range(T):
    P, M, F, C = map(int, input().split())
    coupons = (M//P) * C
    base = coupons//F
    diff = F - C
    x = coupons - F if coupons >= F else 0
    count = x//diff
    res = x%diff + F if coupons >= F else 0
    while res >= F:
        count += 1
        res -= diff
    print(count-base)