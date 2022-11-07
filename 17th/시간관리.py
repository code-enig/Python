# 하루가 어떻게 100만시간인지 모르겠지만...
# 가장 나중에 끝마쳐도 되는 일부터 앞으로 오게끔 정렬
# 가장 나중에 끝마쳐야하는일(A)을 미루고 미뤄서(늦게 일어나고 싶으니까) 기한에 딱맞춰서 끝나게 시작한다고 하고 시작
# 두번째로 나중에 끝마쳐하는 일(B)의 마쳐야 하는 시간(C)을 가져와서, 앞에서 일을 시작한 시간(D)과 비교, 만약 C가 앞서면 두번째로 끝마쳐야 하는일을 앞과 같은 방식으로 시작
# D가 앞서면 일을 시작한 시간 보다 B에 걸리는 시간만큼 앞서 시작해야한다. 
# 이것을 반복하다 0 보다 작아지면 불가능
import sys
sys.stdin = open('17th\\input','r')

N = int(input())
time_table = []
for _ in range(N):
    t1, t2 = map(int,input().split())
    time_table.append((t1,t2))
time_table.sort(key = lambda x : x[1], reverse = True)

latest = 1000000
for i in range(N):
    # 일어나야 하는 시각이 현재 확인중인 일의 끝마쳐야하는 시간보다 얼마나 앞섰는지 알려주는 값 det
    det = time_table[i][1] - latest
    if det >= 0:
        latest -= time_table[i][0]
    else:
        latest = time_table[i][1] - time_table[i][0]
if latest < 0:
    print(-1)
else:
    print(latest)