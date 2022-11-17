import sys
sys.stdin = open('Python\\24th\\input','r')
input = sys.stdin.readline
K = int(input())
n = int(input())
start = [chr(i) for i in range(65,65+K)]
temp = input()
final = [temp[i] for i in range(K)]
answer = ''
rows_up = []
rows_down = []
q = False
for _ in range(n):
    temp = input().rstrip()
    if temp[0] == '?':
        q = True
        continue
    if not q:
        rows_up.append(temp)
    else:
        rows_down.append(temp)
for i in range(len(rows_up)):
    for j in range(K-1):
        if rows_up[i][j] == '-':
            start[j],start[j+1] = start[j+1],start[j]
for i in range(len(rows_down)-1,-1,-1):
    for j in range(K-1):
        if rows_down[i][j] == '-':
            final[j],final[j+1] = final[j+1],final[j]
k = 0
while k < K-1:
    if start[k] == final[k]:
        answer = answer + '*'
        k += 1
    elif start[k] == final[k+1] and start[k+1] == final[k]:
        start[k],start[k+1] = start[k+1],start[k]
        answer = answer + '-'
        k += 1
    else:
        answer = 'x'*(K-1)
        break
print(answer)