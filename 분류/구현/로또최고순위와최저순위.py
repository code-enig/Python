# 추가로 어떠한 숫자도 못맞추면 최저 순위, 모든 숫자를 다 맞추면 최고 순위
def solution(lottos, win_nums):
    set_lottos = set(lottos)
    set_win_nums = set(win_nums)
    min_match = len(set.intersection(set_lottos, set_win_nums))
    max_match = lottos.count(0) + min_match

    answer = [7 - max_match if max_match > 1 else 6,
              7 - min_match if min_match > 1 else 6]
    return answer