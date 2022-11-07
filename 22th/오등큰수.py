import sys
sys.stdin = open('22th\\input','r')
input = sys.stdin.readline
N = int(input())
answer = [-1 for _ in range(N)]
# 입력이 100만 까지이므로, 1 더해주는 것을 잊지말자
num_num = [0 for _ in range(1000001)]
seq = list(map(int, input().split()))

for number in seq:
    num_num[number] += 1

num_stack = []
for i,number in enumerate(seq):
    flag = True
    while num_stack:
        if num_num[number]>num_num[num_stack[-1][1]]:
            index = num_stack.pop()[0]
            answer[index] = number
        else:
            num_stack.append((i,number))
            flag = False
            break
    if flag:
        num_stack.append((i,number))

for number in answer:
    print(number,end=' ')