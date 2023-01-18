# 원의 경계에서 점이 들어가는지 안들어가는지 판단한 후 들어가며 그대로 더하고 그렇디 않으면 -1 해서 더 한다. => // 를 이용한다.
import math
def solution(k, d):
    answer = 0
    for h in range(0,d+1,k):
        answer += math.sqrt((d**2-h**2))//k+1
    answer = int(answer)
    return answer

k, d = 2, 4
print(solution(k, d))
print()
k, d = 1, 5
print(solution(k, d))