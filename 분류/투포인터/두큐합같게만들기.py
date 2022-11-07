# 투포인터... 두큐가 연결된 원형 연결 리스트라고 생각하고 합이 절반이 되는 구간을 찾으면 된다.
def solution(queue1, queue2):
    answer = -1
    q1_first = queue1 + queue2
    q2_first = queue2 + queue1
    if sum(q1_first)%2:
        pass
    else:
        target = sum(q1_first)//2
        l1,l2 = len(q1_first),len(q2_first) # 포인터가 큐 범위를 벗어나지 않게 해줄 최댓값
        p11,p12 = 0,len(queue1)-1 # queue1의 처음과 끝을 표현할 값들
        p21,p22 = 0,len(queue2)-1  # queue2의 처음과 끝을 표현할 값들
        sub_sum1, sub_sum2 = sum(q1_first[:len(queue1)]), sum(q2_first[:len(queue2)])
        counter1, counter2 = 0, 0
        while p12<l1-1: # 뒤 큐를 다 빼서 앞큐에 넣기 전까지
            if sub_sum1 == target:
                answer = counter1
                break
            elif sub_sum1 > target:
                sub_sum1 -= q1_first[p11]
                p11 += 1
                counter1 += 1
            else:
                p12 = (p12+1)%l1
                sub_sum1 += q1_first[p12]
                counter1 += 1
        while p22<l2-1: # 뒤 큐를 다 빼서 앞큐에 넣기 전까지
            if sub_sum2 == target:
                answer = min(answer,counter2) if answer != -1 else counter2
                break
            elif sub_sum2 > target:
                sub_sum2 -= q2_first[p21]
                p21 = (p21+1)%l2
                counter2 += 1
            else:
                p22 = (p22+1)%l2
                sub_sum2 += q2_first[p22]
                counter2 += 1
    return answer
q1,q2 = [1, 1, 1, 1, 1], [1, 1, 1, 9, 1]
print(solution(q1,q2))