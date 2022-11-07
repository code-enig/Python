#DP?
# 열 마다 연결된 물들을 하나의 노드로 취급
# 왼쪽-> 오른쪽으로 노드가 연결 되었는가만 확인
# 오른쪽 노드가 연결 되었으려면 연결된 왼쪽노드가 연결되었어야 한다. ->DP

from sys import stdin
stdin = open('20th\\input', 'r')
input = stdin.readline
N,M = map(int, input().split())
length_list = list(map(int,input().split())) # 각 열의 물정보 길이 리스트
info_list = [list(map(int,input().split())) for _ in range(M)] # 각 열의 연결된 물 정보
node_inf = [[0 for _ in range(length//2)] for length in length_list] # 연결된 물정보는 2개로 표현되므로
for i in range(length_list[0]//2):
    node_inf[0][i] = 1 # 맨왼쪽은 1로 놓고 시작
for i in range(M-1): # 0번 부터 M-2 번 열 노드의 옆 노드를 확인 1열부터 M-1 열까지 확인 
    j, k = 0, 0 # j: 지금 열 노드 번호, K: 다음 열 노드 번호
    while j<len(info_list[i])-1 and k<len(info_list[i+1])-1: # 둘다 범위 내에 있을 때 까지만 탐색
        if node_inf[i][j//2] == 0: # 연결안된 노드라면 탐색할 필요 없음
            j += 2
            continue
        # 노드의 시작과 끝
        now_min,now_max = info_list[i][j], info_list[i][j+1]
        nxt_min,nxt_max = info_list[i+1][k], info_list[i+1][k+1]
        # 노드의 시작과 끝의 배치에 따라서 노드를 건너 뛰어가면서 연결되었음을 표기하고 넘어간다.
        if now_min > nxt_max:
            k += 2
        elif now_max < nxt_min:
            j += 2
        elif now_min <= nxt_max:
            node_inf[i+1][k//2] = 1
            if nxt_max < now_max:
                k += 2
            else:
                k += 2
                j += 2
print(node_inf)
if 1 in node_inf[-1]: # 연결된 물이 하나라도 있으며 YES 였던거임...
    print('YES')
else:
    print('NO')