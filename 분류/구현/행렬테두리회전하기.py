#요구에 따라 행렬을 돌리면서 최저값을 찾는다.
def solution(rows, columns, queries):
    answer = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    matrix = [[(i)*columns + j+1 for j in range(columns)] for i in range(rows)]

    for query in queries:
        x1, y1, x2, y2 = [query[i]-1 for i in range(4)] # 인덱스 맞추기
        # 회전하는 꼭지점들
        check1 = (x1, y1) 
        check2 = (x1, y2)
        check3 = (x2, y2)
        check4 = (x2, y1)
        x, y = x1, y1 #시작은 왼쪽 위
        tmp_value = matrix[x1][y1]
        min_value = tmp_value #최솟값 가정
        for i in range(4): # 우 하 좌 상 으로 회전
            while True:
                x += dx[i]
                y += dy[i]
                matrix[x][y], tmp_value = tmp_value, matrix[x][y] # 한 칸 이동한 뒤 비교할 값 교환
                if tmp_value < min_value:
                    min_value = tmp_value
                if (x, y) == check1 or (x, y) == check2 or (x, y) == check3 or (x, y) == check4: # 꼭지점 체크
                    break
        answer.append(min_value)
    return answer
