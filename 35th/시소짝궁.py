# 2,3,4 -> 3*2/2 -> 4가지 거리 조합>> 같을 때, 2,3 2,4 ,3,4
# 2중 for -> 시간 초과
# weight를 검색 할 때 자신과 밸런스를 이루는 weight 가 있는지 알려주는 배열을 하나 더 만든다.

def solution(weights):
    answer = 0
    check = [0 for _ in range(1001)]
    weights.sort() # 이제 자기보다 작은 애들만 앞에 있다.
    for weight in weights:
        answer += balanced(weight, check)
        check[weight] += 1
    return answer

def balanced(w,c):
    ret = 0
    if c[w]:
        ret += c[w] 
    if not w%2 and c[w//2]:
        ret += c[w//2]
    if not w%3 and c[2*w//3]:
        ret += c[2*w//3]
    if not w%4 and c[3*w//4]:
        ret += c[3*w//4]
    return ret

weights = [100,180,360,100,270]
print(solution(weights))