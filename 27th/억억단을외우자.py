# 일반적인 소인수분해 방식으로 어느 한 숫자의 약수를 구하는 방식은 너무 오래걸림
# 반대로 한수의 약수를 구하는 것이 아닌 어떤 수로 만들수 있는 합성수를 다 구해서 
# 약수의 갯수를 늘리는 방식으로 약수의 갯수를 맞춰나간다.
from collections import defaultdict
import copy
def solution(e, starts):
    answer = []
    divisors=[0 for _ in range(e+1)]
    max_divisors_number = [e for _ in range(e+1)]
    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)): # min(e//i+1,i)=> i,j가 서로 뒤집은 경우가 생기지 않게...?
            divisors[i*j] += 2 # 다른 두 수의 곱으로 이루어진 수의 경우(이 경우 억억단에서 두 번 나옴)

    for i in range(1,int(e**(1/2)+1)):
        divisors[i**2] += 1 # 제곱수의 경우 (이 경우 억억단에서 한 번만 나옴)

    tmp_max = 0
    tmp_max_number = e
    for number in range(e,-1,-1):
        if divisors[number] >= tmp_max:
            tmp_max_number = number
            max_divisors_number[number] = tmp_max_number
            tmp_max = divisors[number]
        else:
            max_divisors_number[number] = tmp_max_number
    for s in starts:
        answer.append(max_divisors_number[s])
    return answer
e, starts = 8,[1,3,7]
print(solution(e, starts))