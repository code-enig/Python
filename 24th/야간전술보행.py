def solution(distance, scope, times):
    answer_list = []
    for i in range(len(scope)):
        enterance_time = min(scope[i]) # i 번째 경비병이 감시하는 구간을 통과하게 된다면 그 때 그 구간에 돌입하는 시간
        exit_time = max(scope[i]) # i 번째 경비병이 감시하는 구간을 통과하게 된다면 그 때 그 구간을 나오는 시간
        pass_time =  exit_time - enterance_time # 통과하는데 걸리는 시간
        period = times[i][0] + times[i][1] # 각 경비병의 주기
        # 구간에 진입할 때 경비가 휴식에 들어갔을지 아닐지 판단해줄 값, 
        # 그 구간까지 오는데 걸린 시간을 경비병의 경계 주기나눈 나머지 값, 경비병이 마지막 휴식을 취하고 얼마나 지났는지 알려주는 값
        # det <= times[i][0] 이면 근무중 , period로 나누어 떨어지면 들어가는 순간에는 근무중이 아님
        det = enterance_time%period if enterance_time%period else period
        if det <= times[i][0]: answer_list.append(enterance_time)
        # 위 경우가 아니면 경비병은 일단 휴식 중. 그런데, 통과하는데 걸리는 시간(pass_time)이 길어서, 
        # det+pass_time이 주기보다 길어지면, 경비병은 다시 근무를 서고 발각된다.
        elif det + pass_time > period:
            # 감시를 재개(+1)하면 휴식 다음 주기에 바로 발각 된다.
            if enterance_time%period: answer_list.append((enterance_time//period+1)*period + 1)
            else: answer_list.append((enterance_time//period)*period + 1)
    else:
        answer_list.append(distance)# 무사히 통과
    answer_list.sort()
    answer = answer_list[0]
    return answer

distance, scope, times = 10,[[3, 4], [5, 8]],[[2, 5], [4, 1]]
print(solution(distance, scope, times))
distance, scope, times = 12,[[7, 8], [4, 6], [11, 10]],[[2, 2], [2, 4], [3, 3]]
print(solution(distance, scope, times))