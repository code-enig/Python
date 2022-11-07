import sys
sys.stdin = open('22th\\input','r')
input = sys.stdin.readline
N,M = map(int, input().split())
board = [[0 for i in range(M+6)] for j in range(3)]
for _ in range(N):
    board.append([0,0,0]+list(map(int, input().split()))+[0,0,0])
board.extend([[0 for i in range(M+6)] for j in range(3)])
answer = 0
for i in range(3,N+3):
    for j in range(3,M+3):
        # cyan
        answer = max(answer, board[i][j]+board[i][j+1]+board[i][j+2]+board[i][j+3],board[i-3][j]+board[i-2][j]+board[i-1][j]+board[i][j])
        #yellow
        answer = max(answer, board[i][j]+board[i+1][j]+board[i][j+1]+board[i+1][j+1])
        #orange, 그대로
        answer = max(answer, board[i][j]+board[i+1][j]+board[i+2][j]+board[i+2][j+1],board[i][j]+board[i-1][j]+board[i-2][j]+board[i-2][j-1],board[i][j]+board[i][j+1]+board[i][j+2]+board[i-1][j+2],board[i][j]+board[i][j-1]+board[i][j-2]+board[i+1][j-2])
        #orange, 대칭
        answer = max(answer, board[i][j]+board[i+1][j]+board[i+2][j]+board[i+2][j-1],board[i][j]+board[i-1][j]+board[i-2][j]+board[i-2][j+1],board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+2],board[i][j]+board[i][j-1]+board[i][j-2]+board[i-1][j-2])
        #green, 그대로
        answer = max(answer, board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+2][j+1],board[i][j]+board[i][j+1]+board[i-1][j+1]+board[i-1][j+2])
        #green, 대칭
        answer = max(answer, board[i][j]+board[i+1][j]+board[i+1][j-1]+board[i+2][j-1],board[i][j]+board[i][j-1]+board[i-1][j-1]+board[i-1][j-2])
        #magenta, 그대로
        cross = board[i][j]+board[i+1][j]+board[i][j+1]+board[i-1][j]+board[i][j-1]
        answer = max(answer,cross-board[i+1][j],cross-board[i][j+1],cross-board[i-1][j],cross-board[i][j-1])
print(answer)
