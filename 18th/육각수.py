# DP
# 계차수열 일반항 -> n^2 -< 생각보다 1백만보다 작은 육각수 숫자가 적음 ->707개,271개 -> 707C3 = 약 5천만, 271C4 = 약 2억 -> 제한시간 2초니까 어떻게 될꺼 같음
# 146858 보다 크면 2개 또는 3개로 가능
# 130 보다 크면 4개 안쪽으로 가능
# 26 보다 크면 5개 안쪽으로 가능
import sys
sys.stdin = open('18th\\input','r')
input = sys.stdin.readline

N = int(input())

hex = []
number = [7 for _ in range(N+1)]
i=0
while True: # 육각수 생성
    i += 1
    elem = i*(2*i-1)
    if elem > N:
        break
    hex.append(elem)

for elem in hex:
    number[elem] = 1

for n in range(1,N+1):
        if number[n] == 1: # 육각수로 만들수 있는 숫자들
            for elem in hex:
                if n+elem < N+1:
                    number[n+elem] = 2 if number[n+elem] != 1 else 1 # 육각수 2개로 만들수 있는 숫자들
if N <= 146858:
    for n in range(1,N+1):
        if number[n] in [1,2]: # 육각수 1개 또는 2개로 만들 수 있는 숫자들
            for elem in hex:
                if n+elem < N+1:
                    number[n+elem] = number[n]+1 if number[n]+1 < number[n+elem] else number[n+elem] # 육각수 2개 또는 3개로 만들 수 잇는 숫자들
    if N <=130:
        for n in range(1,N+1):
            if number[n] in [1,2,3]:
                for elem in hex:
                    if n+elem < N+1:
                        number[n+elem] = number[n]+1 if number[n]+1 < number[n+elem] else number[n+elem]
        if N <=26:
            for n in range(1,N+1):
                if number[n] in [1,2,3,4]:
                    for elem in hex:
                        if n+elem < N+1:
                            number[n+elem] = number[n]+1 if number[n]+1 < number[n+elem] else number[n+elem]
            print(min(number[N],6))
        else:
            print(min(number[N],5))
    else:
        print(min(number[N],4))
else:
    print(min(number[N],3))