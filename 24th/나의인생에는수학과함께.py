# dp[n][m] = [max, min]으로 짠다.
# 어떤 지점에는 4가지 방법으로 도달할 수 있다. dp[n-1][m-1]에서 2가지 경로 dp[n][m-1]에서 dp[n-1][m]에서 각 하나의 경로
# 점화식은 대충 아래와 같다.
# max = 8가지 경우 중 최댓값
# min = 8가지 경우 중 최솟값
import sys
sys.stdin = open('Python\\24th\\input','r')
input = sys.stdin.readline
N = int(input())
INF = 5**5

# 예외 만들기 귀찮으므로 있을수없는 값으로 주변을 둘러싼다.
board = [[INF,'*']*(N//2+2)+[INF]]
board.append(['*',INF]*(N//2+2)+['*'])
for _ in range(N):
    board.append([INF,INF]+list(input().split())+[INF,INF])
board.append(['*',INF]*(N//2+2)+['*'])
board.append([INF,'*']*(N//2+2)+[INF])

dp = [[[INF,INF] for i in range(N+4)] for j in range(N+4)]

# 연산자와 값을 집어넣으면 가능한 값들을 리스트로 돌려주는 함수
def operation(oper, num_list, n):
    result = []
    if oper == '*':
        for num in num_list:
            if num >= INF :
                continue
            result.append(num*n)
    elif oper == '+':
        for num in num_list:
            if num >= INF:
                continue
            result.append(num+n)
    elif oper == '-':
        for num in num_list:
            if num >= INF:
                continue
            result.append(num-n)
    return result

dp[2][2] = [int(board[2][2]),int(board[2][2])]
for i in range(2,N+2):
    for j in range(2,N+2):
        if (i+j)%2 or (i==2 and j==2):
            continue
        num_list = [[],[]]
        [n1,n2],[n3,n4],[n5,n6] = dp[i-2][j],dp[i-1][j-1],dp[i][j-2]
        combs = []
        combs.extend(operation(board[i-1][j],[n1,n2,n3,n4],int(board[i][j])))
        combs.extend(operation(board[i][j-1],[n3,n4,n5,n6],int(board[i][j])))
        dp[i][j][0] = max(combs)
        dp[i][j][1] = min(combs)

for n in dp[N+1][N+1]:
    print(n,end= ' ')