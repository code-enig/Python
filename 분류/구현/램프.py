# 행의 구조가 같아야 같이 켜질수 있다. 01010이 테스트할 행일 경우 01010 만이 같이 꺼지고 켜질수 있다.
import sys
sys.stdin = open('11th\\input','r')
N, M = map(int,sys.stdin.readline().split())
table = []

for _ in range(N):
    tmp = sys.stdin.readline()
    tmp_list = []
    for i in range(M):
        tmp_list.append(int(tmp[i]))
    table.append(tmp_list)
K = int(sys.stdin.readline())
answer = 0

for i in range(N):
    count = 0
    comparison = table[i] # 비교 대상이 될 행 
    offs = table[i].count(0) # 그 행을 켜는데 필요한 횟수
    # 모두 짝수이거나 모두 홀수이면 필요한 스위치를 다 키고나서 남는 횟수는 스위치 하나를 정해서 껐다 켜는것으로 소모 가능
    if offs <= K and offs%2 == K%2:
        for j in range(N):
            if comparison == table[j]:
                count += 1
        answer = max(answer, count) # 최댓값 찾기      
print(answer)