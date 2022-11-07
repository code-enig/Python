from collections import defaultdict
def solution(clothes):
    answer = 1
    cloth_dict = defaultdict(int)
    for cloth in clothes:
        cloth_dict[cloth[1]] += 1
    print(cloth_dict)
    for v in cloth_dict.values():
        answer *= v+1
    return answer-1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))