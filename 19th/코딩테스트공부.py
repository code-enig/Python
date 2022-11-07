#DP?
def solution(alp, cop, problems):
    answer = 0
    max_alp_req = 0
    max_cop_req = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp_req = max(max_alp_req, alp_req)
        max_cop_req = max(max_cop_req, cop_req)
    alp = min(alp,max_alp_req)# DP 를 시작할 값, 이미 만족하면 할 필요가 없다.
    cop = min(cop,max_cop_req)
    INF = float('inf')
    time_req = [[INF for i in range(max_cop_req+1)] for j in range(max_alp_req+1)] # 배열[알고력, 코딩력] = 도달하는데 필요한 시간, 알고력이나 코딩력=0 존재
    time_req[alp][cop] = 0 # 현재 알고력과 코딩력은 이미 달성한 상태이므로 시간 0
    for i in range(alp, max_alp_req+1): # 더 높은 코딩력과 더 높은 알고력만 보면 되므로
        for j in range(cop, max_cop_req+1):
            # 평범한 방법 선택
            if i < max_alp_req and j <= max_cop_req:
                time_req[i+1][j] = min(time_req[i+1][j], time_req[i][j]+1) # 알고리즘을 공부
            if i <= max_alp_req and j < max_cop_req:
                time_req[i][j+1] = min(time_req[i][j+1], time_req[i][j]+1) # 코딩을 공부
            # 그보다 좋은 방법이 있는지 검색
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req: # 풀수 있는 문제라면
                    nxt_alp, nxt_cop = min(i+alp_rwd,max_alp_req),min(j+cop_rwd,max_cop_req)
                    time_req[nxt_alp][nxt_cop] = min(time_req[nxt_alp][nxt_cop], time_req[i][j] + cost)
    answer = time_req[-1][-1]
    return answer

alp,cop,problems = 0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]

print(solution(alp, cop, problems))