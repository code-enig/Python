# 다익스트라 -> 언제 끊어야 하나?
# set 사용하면 비트마스크와 같은 속도
# 다익스트라 힙 사용한 알고리즘 ElogV 속도 -> 20만*log5만 => 100만
import heapq
MAX = 10000001

def solution(n, paths, gates, summits):
    answer = [n+1,MAX] 
    node_inf = [[]for _ in range(n+1)]
    for path in paths:
        node_inf[path[0]].append((path[1],path[2]))
        node_inf[path[1]].append((path[0],path[2]))

    summits = set(summits)
    gates = set(gates)
    intensity =[]
    min_time = [MAX for _ in range(n+1)]
    for gate in gates: # 모든 출입구를 힙에 넣고 시작, 계산낭비 줄임
        heapq.heappush(intensity, [0,gate])
        min_time[gate] = 0
 
    while intensity: # 갱신할 지점이 없어질 때까지
        time,node = heapq.heappop(intensity) # 갱신 기준점
        if node in summits: # 산봉우리 만나면 탈출
            if time < answer[1]:
                answer = [node,time]
            elif time == answer[1] and node < answer[0]:
                answer = [node,time]
            continue
        # 1과 2에 시간 차이가 존재해서 
        # 갱신하다 보니 이번 노드 차례가 오기전에 이번 노드가 갱신을 한차례 이상 더 갱신을 당한 경우가 생길 수 있음
        # 이 경우 오래된 정보로 노드를 갱신할 필요가 없으므로 스킵
        if min_time[node] < time: 
            continue
        for nxt in node_inf[node]:
            nxt_node,nxt_time = nxt
            nxt_time = max(nxt_time, time) if nxt_time != MAX else time
            if nxt_node in gates: # 출입구 만나면 탈출
                continue
            if min_time[nxt_node] <= nxt_time: # 다음노드 갱신전에 이미 갱신해서 만들어질 상태보다 시간이 짧다면
                continue
            min_time[nxt_node] = nxt_time # 1.즉시 갱신
            heapq.heappush(intensity,[nxt_time,nxt_node]) # 2.다음 힙 차례가 와야 갱신 된걸 확인 가능

    return answer


n,paths, gates, summits = 5,[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],[1, 2],[5]

print(solution(n, paths, gates, summits))