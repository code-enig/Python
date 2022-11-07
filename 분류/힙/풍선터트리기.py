# 만약 수열을 (영역1)최솟값1(영역2)최솟값2(영역3) 으로 표시한다면. 영역2 에 있는 숫자들은 절대 불가능
# (영역1) 에서는 자기 기준으로 왼쪽 값이 다 자기보다 크면 가능
# (영역2) 에서는 자기 기준 오른쪽 값이 다 자기보다 크면 가능
import heapq
import copy
def solution(a):
    answer = 0
    flag = False # 탈출 조건: 두 최솟값중에 하나를 만나면 달성
    heap_a = copy.deepcopy(a)
    heapq.heapify(heap_a)
    # 자기를 기준으로 자기의 숫자가 제일 작은 풍선이면 무조건 다 터트릴수 있다. 두번째로 작은 풍선 첫번째 빼고 다 터트릴수 있다.
    # 세번째 부터는 불가능
    first_min = heapq.heappop(heap_a) # 제일 작은 값
    second_min = heapq.heappop(heap_a) # 두번째로 작은 값
    left_min = a[0] # 그 값을 기준으로 왼쪽에 있는 숫자들의 최솟값
    i = 0 # 왼쪽 끝부터 검색 시작
    while True:
        if flag:
            if a[i] == first_min or a[i] == second_min: # 첫번째나 두번째 최솟값을 만나면 탈출한다.
                flag = not flag
                break
        if a[i] == first_min or a[i] == second_min:
            answer += 1
            flag = not flag
            continue
        if a[i] <= left_min:
            left_min = a[i]
            answer +=1
        i += 1
        if i > len(a)-1: break

    j = len(a)-1 #오른쪽 끝부터 검색
    right_min = a[j] #기준에서 오른쪽의 최솟값
    while True:
        if flag:
            if a[j] == first_min or a[j] == second_min:
                break
        if a[j] == first_min or a[j] == second_min:
            answer += 1
            flag = not flag
            continue
        if a[j] <= right_min:
            right_min = a[j]
            answer +=1
        j -= 1
    return answer

a = [9,-1,-5]
print(solution(a))