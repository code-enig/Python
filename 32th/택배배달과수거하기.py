# 가장 먼 곳 부터 처리하는 것이 좋다.
def solution(cap, n, deliveries, pickups):
    answer = 0
    d = deliveries
    p = pickups
    d_index = n-1 # 배달해야할 집들 중 마지막 집
    p_index = n-1 # 수거해야할 집들 중 마지막 집
    while not d[d_index] and d_index >= 0: #초깃값 찾기
        d_index -= 1
    while not p[p_index] and p_index >= 0: #초깃값 찾기
        p_index -= 1
    tot_deliveries = sum(deliveries) #초깃값 설정
    completed_deliveries = 0 #초깃값 설정
    while d_index>=0 or p_index>=0: # 모든매달이 끝날 때 까지
        d_boxes = min(cap, tot_deliveries-completed_deliveries) # 트럭에 실을 배달박스의 숫자
        completed_deliveries += d_boxes# sum([:]) 함부로 쓰지 말것 , O(N) 연산시간
        if d_index >= p_index: # 가장 먼곳이 배달해야할 집이라면 그 집까지 배달하러 갔다가(+1) 돌아와야(+1)하므로 *2
            answer += 2*(d_index+1)
        else:
            answer += 2*(p_index+1) # 가장 먼곳이 회수해야할 집이라면
           
        while d_boxes and d_index >=0:
            if d[d_index] > d_boxes: # 배달해야할 박스가 지금 현재 트럭에 실린 박스의 양보다 많다면
                d[d_index] -= d_boxes # 일단 다 배달하고
                d_boxes = 0
            else:
                d_boxes -= d[d_index] # 배달을 하고
                d[d_index] = 0 # 배달 완료 (순서 중요!)     
                d_index -= 1
                
        c = cap # 트럭의 여유 공간, 이미 오는길에 박스를 다 내려주었으므로 택배수거 차량은 비어있다.
        while c and p_index >= 0:
            if p[p_index] > c:
                p[p_index] -= c
                c = 0
            else:
                c -= p[p_index]
                p[p_index] = 0            
                p_index -= 1
                
        while not d[d_index] and d_index>=0: # 인덱스 수정, 수거하거나 배달할 박스가 없는 집들을 제외
            d_index -= 1
        while not p[p_index] and p_index>=0:
            p_index -= 1
    return answer

cap, n, deliveries, pickups = 4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0]
print((solution(cap, n, deliveries, pickups)))
cap, n, deliveries, pickups = 2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]
print((solution(cap, n, deliveries, pickups)))