#해시, defaultdict을 활용한 초기화
from collections import defaultdict
def solution(participant, completion):
    com_dict = defaultdict(int)
    answer = ''
    for name in completion:
        com_dict[name] += 1
    for name in participant:
        com_dict[name] -= 1
        if com_dict[name] < 0:
            answer = name
    return answer