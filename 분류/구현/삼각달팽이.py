#진행 방향을 돌리려고 데크사용
from collections import deque
def solution(n):
    delta = deque([[1,0],[0,1],[-1,-1]])
    answer =[] 
    triangle=[[0 for i in range(j)] for j in range(1,n+1)]
    order = [0,0]
    start = 1
    stop_value = n*(n+1)/2
    keepgoing = True
    value = start
    height = len(triangle)
    width = len(triangle[-1])
    while keepgoing:     
        triangle[order[0]][order[1]] = value
        value += 1
        if value > stop_value:
            keepgoing = False
            break
        next_y = order[0] + delta[0][0]
        next_x = order[1] + delta[0][1]
        if next_y > height-1 or next_x > width-1 or triangle[next_y][next_x]: # 벽이나 다른 숫자를 만나면
            delta.rotate(-1)
            next_y = order[0] + delta[0][0]
            next_x = order[1] + delta[0][1]
        order[0] = next_y
        order[1] = next_x
    for line in triangle:
        answer.extend(line)
    return answer

print(solution(5))