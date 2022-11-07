#구현
def solution(line):
    answer = []
    INF = float('inf')
    intersections = []
    x_min,x_max,y_min,y_max = INF,-INF,INF,-INF
    # 교점찾기, 자기 자신을 제외한 모든 직선과 1000*999/2 번 연산
    for i,(a1,b1,c1) in enumerate(line):
        for a2,b2,c2 in line[i+1:]:
            det = a1*b2 - b1*a2
            if det:
                x = (b1*c2-b2*c1)
                y = (a2*c1-a1*c2)
                if not x%det and not y%det: # 정수인 경우만 찾는다고 하였으므로
                    x,y = x//det, y//det
                    x_min, x_max, y_min, y_max = min(x,x_min), max(x,x_max), min(y,y_min), max(y,y_max) #최대,최소 찾기
                    intersections.append((x,y))
    answer_board = [['.' for i in range(x_min,x_max+1)] for j in range(y_min,y_max+1)] #일단 다 . 으로 채워넣은 배열 만들기
    for intersection in intersections:
        x,y = intersection
        answer_board[y_max-y][x-x_min] = '*'
    for answer_line in answer_board:
        answer.append(''.join(answer_line)) # 배열을 문자열로
    return answer

line = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
board = solution(line)

for l in board:
    print(l)