import sys
sys.stdin = open('Python\\input','r')
N,d,k,c = map(int,sys.stdin.readline().split())
belt = []
sushi_types = [0 for _ in range(d)]
max_types = 0

for _ in range(N):
    belt.append(int(sys.stdin.readline()))
belt.extend(belt[:k])

for i in range(k):
    sushi_types[belt[i]-1] += 1
num_exist_types = d - sushi_types.count(0)

for i in range(N):
    if sushi_types[c-1]:
        max_types = max(max_types,num_exist_types)
    else:
        max_types = max(max_types,num_exist_types+1)
    sushi_types[belt[i]-1] -= 1
    if sushi_types[belt[i]-1] == 0:
        num_exist_types -= 1
    if sushi_types[belt[i+k]-1] == 0:
        num_exist_types += 1
    sushi_types[belt[i+k]-1] += 1
    
print(max_types)