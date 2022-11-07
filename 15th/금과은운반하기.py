# ?? 이분탐색
# 시간 t 이후에 금과 은을 그만큼 옮길수 있느냐 없느냐
# max_t 의 설정: (2*10^9)*(5*10^5)/1 광물 최대양*최장시간 / 한번에 옮길수 있는 양 으로 설정
# t 시간후 옮길수 있는 최대 광물의 양:
# t 시간후 옮길수 있는 최대 은의 양:
# t 시간후 옮길수 있는 최대 금의 양:
global max_t
max_t = (2*10**9)*(5*10**5)
global start_t
start_t = 0

def solution(a, b, g, s, w, t):
    global max_t, start_t
    answer = -1
    if start_t == max_t:
        return start_t
    mid = (start_t+max_t)//2
    if possible(mid,a, b, g, s, w, t):
        max_t = mid
        answer = solution(a, b, g, s, w, t)
    else:
        start_t = mid + 1
        answer = solution(a, b, g, s, w, t)

    return answer
    
def possible(time_t,a, b, g, s, w, t):
    num_city = len(g)
    amount_all = 0
    amount_gold = 0
    amount_silver = 0
    for city in range(num_city):
        #max_t 시간후 옮긴 광물의 양
        # 모든 광물을 다 옮기는 데 필요한 '왕복' 횟수, 처음은 편도
        n_all = (g[city]+s[city])//w[city]
        n_gold = g[city]//w[city]
        n_silver = s[city]//w[city]
        # 왕복에는 편도 시간의 2배가 든다
        if time_t > t[city] +2*t[city]*n_all: # 시간이 충분하면 모든 광물을 옮길수 있다.
            amount_all += g[city]+s[city]
        else:
            amount_all += (w[city] + w[city]*((time_t-t[city])//(2*t[city])) if time_t >= t[city] else 0)

        if time_t > t[city] + 2*t[city]*n_gold:
            amount_gold += g[city]
        else:
            amount_gold += (w[city] + w[city]*((time_t-t[city])//(2*t[city])) if time_t >= t[city] else 0)

        if time_t > t[city] + 2*t[city]*n_silver:
            amount_silver += s[city]
        else:
            amount_silver += (w[city] + w[city]*((time_t-t[city])//(2*t[city])) if time_t >= t[city] else 0)

    if amount_all >= a+b and amount_gold >= a and amount_silver >= b:
        return True
    else:
        return False
a, b, g, s, w, t = 10,10,[100],[100],[7],[10]

print(solution(a, b, g, s, w, t))