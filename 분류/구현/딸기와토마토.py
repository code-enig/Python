#1. 행과 열 모두 존재하는 경우 
# 행이나 열이 겹치지 않고 있는 경우 => 0
# 행과 열이 있다면 교차점

#2. 행과 열중 하나만 존재하는 경우
# 행 또는 열 뿐이 없다면 겹치는 영역만
# 2행이나 2열이 있는 경우 =>0
import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int, input().split())
sat = [list(map(int, input().split())) for _ in range(N)]
row = []
row_exist = False
column = []
column_exist = False

for i in range(N):
    temp = deque()
    start = 0
    end = 0
    temp_length = 0
    for j in range(M):
        if end and sat[i][j]:
            print(0)
            sys.exit(0)
        if sat[i][j]:
            temp_length += 1
            if not start:
                start = j+1    
            if j+1-start+1 > K:
                temp.popleft()
            else:
                temp.append([i+1,j+1])
        elif start:
            end = j-1
    if temp_length >= K:
        if row:
            print(0)
            sys.exit(0)
        row = temp
        row_exist = True

for j in range(M):
    temp = deque()
    start = 0
    end = 0
    temp_length = 0
    for i in range(N):
        if end and sat[i][j]:
            print(0)
            sys.exit(0)
        if sat[i][j]:
            temp_length += 1
            if not start:
                start = i+1
            if i+1-start+1 > K:
                temp.popleft()
            else:
                temp.append([i+1,j+1])
        elif start:
            end = i-1
    if temp_length >= K:
        if column:
            print(0)
            sys.exit(0)
        column = temp
        column_exist = True

if row_exist and not column_exist:
    print(len(row))
    for r,c in row:
        print(r,c)
elif column_exist and not row_exist:
    print(len(column))
    for r,c in column:
        print(r,c)
elif len(column) == K and len(row) == K:
    point = (row[0][0], column[0][1])
    if column[0][0] > point[0] or column[-1][0] < point[0] or row[0][1] > point[1] or row[-1][1] < point[1]:
        print(0)
    else:
        print(1)
        print(row[0][0],column[0][1])
        sys.exit(0)
else:
    print(0)

