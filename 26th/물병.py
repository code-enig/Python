# 2진수 변환
import sys
N,K = map(int,sys.stdin.readline().split())

def wb_num(n,k):
    left_b_digit = 0
    now_b_digit = 23
    count = 0
    while now_b_digit >= 0:
        if n & (1<<now_b_digit):
            count += 1
            if count == k:
                left_b_digit = now_b_digit
        now_b_digit -= 1
        if count > K:
            return 2**(left_b_digit)-(n&(2**(left_b_digit)-1))
    return 0

print(wb_num(N,K))