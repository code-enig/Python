# 결국 N개의 숫자를 M개의 그룹으로 분할해서 최대한 균등하게 맞춰야 하는 문제
# 충전에 걸리는 시간은 k:0~15 까지 총 16종류로 분류 가능
# 2**k = 2**(k-1) *2 이므로 밑에꺼 2개로 위에꺼 하나 커버 가능
# 우선 k:0~15로 전부 센 뒤에, k = 15 부터 M 분할 한다. 부족하면 밑에서 꺼내온다.
import sys
sys.stdin = open('Python\\input','r')
N,M = map(int,sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

def digit(n):
    for bi_digit in range(16):
        if n&(1<<bi_digit):
            break
    return bi_digit

def solution(k,ru):
    global tl
    global charging_time
    if k == 0:
        if tl[k] > 2*ru:
            charging_time += (tl[k]-2*ru)//M
            charging_time += 1 if (tl[k]-2*ru)%M else 0
        return

    charging_time += (2**k)*(tl[k]//M)
    charging_time += (2**k) if tl[k]%M else 0
    
    if not ru:
        required_under = 2 * (M - tl[k]%M) if tl[k]%M else 0
    else:
        required_under = 2 * ru

    if tl[k-1] >= required_under:
        tl[k-1] -= required_under
        solution(k-1,0)
        return
    else:
        required_under -= tl[k-1]
        tl[k-1] = 0
        solution(k-1,required_under)
        return
    

global charging_time
charging_time = 0

global tl
tl = [0 for _ in range(16)]
for time in times:
    tl[digit(time)] += 1
solution(15, 0)
print(charging_time)