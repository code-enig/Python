# 구현
import sys
sys.stdin = open('15th\\input','r')
N = int(input())
global dx, dy
dx = [1,0,-1,0]
dy = [0,1,0,-1]
global class_room
class_room = [[0 for i in range(N)] for j in range(N)]
global friends_list
friends_list = [[] for _ in range(N**2+1)]
students = []

for _ in range(N**2):
    student, friend1, friend2, friend3, friend4 = map(int, input().split())
    students.append(student)
    friends_list[student] = [friend1, friend2, friend3, friend4]

def FriendScore(student, coordinate):
    number = 0
    score = [0,1,10,100,1000]
    y,x = coordinate
    for i in range(4):
        if 0<=y+dy[i]<=N-1 and 0<=x+dx[i]<=N-1:
            if class_room[y+dy[i]][x+dx[i]] in friends_list[student]:
                number +=1
    return score[number]

def Func(student):
    global dx, dy, class_room, friends_list
    position1 = []
    position23 = []
    score = 0
    # 1번 조건
    for i in range(N):
        for j in range(N):
            if class_room[i][j]:
                continue
            coordinate = (i,j)
            friend_score = FriendScore(student,coordinate)
            if  friend_score > score:
                position1 = [coordinate]
                score = friend_score
                continue
            if friend_score == score:
                position1.append(coordinate)
    # 2번, 3번 조건
    empty_score = -1
    for position in position1:
        y,x = position
        empty = 0
        for i in range(4):
            if 0<=y+dy[i]<=N-1 and 0<=x+dx[i]<=N-1:
                if not class_room[y+dy[i]][x+dx[i]]:
                    empty += 1
        if empty > empty_score:
            position23 = position
            empty_score = empty
            continue
    return position23

for student in students:
    position = Func(student)
    class_room[position[0]][position[1]] = student

score = 0
for i in range(N):
    for j in range(N):
        score += FriendScore(class_room[i][j],(i,j))
print(score)