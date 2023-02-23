# DP, 스트링 편집 거리
# 앞에서 부터 문자열을 읽어 나가면서 마지막 문자를 그 순서에 맞는 문자로 만들 때 필요한
# 추가, 삭제, 변환 3 가지 수정 횟수의 합이 최소가 점수를 계산한다.
# DP인 이유: 수정이 일어나기 전까지 점수 + 이번 수정에 필요한 점수 = 총 점수로 되기 때문에
# 예를들어 aab를 baaa 로 상호 쌍방으로 바꾼다 하면, 직관적으로 2점이 최소 필요 점수임을 알수 있다. 
# 이를 DP로 풀어 보면
# P[i][j] = min((p[i-1][j]+1),p[i-1][j-1]+e,p[i][j-1]+1) 이다.// 앞에서부터 삭제,변환,추가
# e = 1 그 변환이 필요하면 필요하지 않으면 0
#     b a a a       a a b
#   0 1 2 3 4     0 1 2 3
# a 1 1 1 2 3   b 1 1 2 2
# a 2 2 1 1 2   a 2 1 1 2
# b 3 2 2 2 2   a 3 2 1 2
#               a 4 3 2 2

from sys import stdin
stdin = open("Python\\input",'r')
n,m = map(int, stdin.readline().split())
submit = stdin.readline().rstrip()
answer = stdin.readline().rstrip()

def score_s_to_a(s, a, n, m):
    dp_table = [[i for i in range(m+1)]]
    dp_table.extend([[j]+[0 for _ in range(m)] for j in range(1,n+1)])
    for r in range(1,n+1):
        for c in range(1,m+1):
            if recognize(s[r-1],a[c-1]):
                dp_table[r][c] = dp_table[r-1][c-1]
            else:
                dp_table[r][c] = min(dp_table[r-1][c]+1,dp_table[r-1][c-1]+1,dp_table[r][c-1]+1)
    return dp_table[n][m]

def recognize(a, b):
    if a == b :
        return True
    if a == 'i' and b in ['i','j','l']:
        return True
    if a == 'v' and b in ['v','w']:
        return True
    return False

print(score_s_to_a(submit, answer, n, m))