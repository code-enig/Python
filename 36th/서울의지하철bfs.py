# dfs bfs-> 최단 거리가 아닌 최소 환승 dfs 해야하나?, 최소환승 BFS가 가능한가?
# 역번호 범위는 2^32-1 로 매우크지만 갯수는 <100 이므로 set 사용
# 양방향
import sys
from collections import defaultdict,deque
sys.stdin = open('input','r')
n = int(sys.stdin.readline())
sts_all_connect = defaultdict(set) # 호선 가리지 않고 모든 역 연결 정보, 노선을 공유하지 말란말이 없었음
sts_transfer_line = defaultdict(list) # { 환승역: 가능한 호선 리스트}
sts = set() # 모든 역
start_lines = []

for i in range(1,n+1):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(tmp)):
        if tmp[j] == 0:
            start_lines.append(i)
        sts.add(tmp[j])
        if j < len(tmp)-1:
            sts_all_connect[tmp[j]].add(tmp[j+1])
            sts_all_connect[tmp[j+1]].add(tmp[j]) # 양방향 이동 가능
        sts_transfer_line[tmp[j]].append(i)

dt = int(sys.stdin.readline())

visited = {st:10 for st in sts} # 그 역에 도달할 때 환승 횟수 (지하철 라인수보다 환승을 더 할수는 없다.)
answer = 10
for start_line in start_lines: # 어떤 지하철 호선을 첫번째로 탔느냐에 따라서... 서울역이 환승역일 가능성
    q = deque([[0,start_line, 0]]) # 역번호, 호선, 환승 횟수
    visited[0] = 0
    while q:
        st_now,l,tf_num = q.popleft()
        for nxt_st in list(sts_all_connect[st_now]):
            if tf_num < visited[nxt_st]: # 저번보다 적은 환승횟수로 방문한다면
                for line in sts_transfer_line[nxt_st]:
                    if line == l:
                        visited[nxt_st] = tf_num
                        if nxt_st == dt:
                            break # 이 지하철호선을 타고 다음 역이 목적지라면 다른 어떤 루트도 이보다 환승이 적을순 없다.
                        q.append([nxt_st,l,tf_num])
                    else:
                        if tf_num+1 < visited[nxt_st]:
                            visited[nxt_st] = tf_num+1
                            q.append([nxt_st,line,tf_num+1])

    answer = min(answer,visited[dt]) if visited[dt] != 10 else -1
print(answer)