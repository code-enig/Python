# 이진탐색, 최솟값을 이진 탐색으로 찾는다. 
# 모든 그룹을 이 점수 이상으로 맞출수 있어? YES -> 최솟값 상승
#                                        NO -> 최댓값 감소
import sys
sys.stdin = open('17th\\input','r')
input = sys.stdin.readline

N, K = map(int, input().split())
scores = list(map(int,input().split()))
max_score = sum(scores)//K # 모든 그룹이 평균 값일 때 최고 점수, 점수 합계가 소수점 이하가 나올수 없으므로 소수점 이하는 버린다.
min_score = 0
while min_score <= max_score:
    score = (min_score+max_score)//2
    sum_score = 0
    count_group = 0
    # 순서대로 그룹을 만든다. 만약 그룹내의 점수가 타겟 점수보다 높아지면 그룹만들기를 끝내고 새로운 그룹으로 넘어간다.
    for i in range(N):
        sum_score += scores[i]
        if sum_score >= score:
            sum_score = 0
            count_group += 1
        # K 그룹 이상 만들어짐을 확인하면, 최솟값을 올린다.
        if count_group == K:
            min_score = score + 1
            break
    else:
        # K 그룹 미만으로 만들어진다면, 최댓값을 내린다.
        max_score = score - 1
# 점수를 올려보다가 최고점수를 넘어버리면 안되므로, 그 직전 점수를 답으로 반환
print(min_score-1)