# -1로 시작열과 시작행을 감싸서 시작열과 시작행이 막혔을때 생기는 오류 제거
# 행과 열 역전 주의
def solution(m, n, puddles):
    answer = 0
    board = [[-1 for _ in range(m+1)]]
    for _ in range(n):
        board.append([-1]+[0 for i in range(m)])
    board[1][1] = 1
    for c,r in puddles:
        board[r][c] = -1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if board[i][j]<0:
                continue
            board[i][j] += board[i-1][j] if board[i-1][j] > 0 else 0
            board[i][j] += board[i][j-1] if board[i][j-1] > 0 else 0
    answer = board[-1][-1]%1000000007
    return answer