# 최대 금액인 1만원도 5번만 상납하면 사라짐. 깊이가 최대 5이므로 for-while로 가능
def solution(enroll, referral, seller, amount):
    answer = [0 for i in range(len(enroll))]
    network = {}
    for i in range(len(enroll)):
        network[enroll[i]] = [referral[i], i] # 추친인과 자신의 인덱스를 딕셔너리에 담는다.

    for i in range(len(seller)):
        lower = seller[i] # 제일 아래에 있는 판매자
        raw_profit = amount[i]*100 # 원래 이익
        share = raw_profit//10 # 상납금

        while network[lower][0] != '-': # 추천인이 더이상 나오지 않을 때까지
            answer[network[lower][1]] += raw_profit - share # 판매자의 수익은 상납금을 제외한 금액이다.
            lower = network[lower][0] # 상납한 금액을 이익으로 가지는 추천인
            raw_profit = share # 상납금을 이득으로
            share = raw_profit//10 # 상납금의 상납금
            if share <=0: # 그런데 상납하다가 상납금이 1의자리가 되면 절삭하므로
                break
        answer[network[lower][1]] += raw_profit - share # 설립자에게 상납 완료

    return answer