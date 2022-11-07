# 구현
import sys
sys.stdin = open('15th\\input','r')

dy = (0,0,-1,-1,-1,0,1,1,1)
dx = (0,-1,-1,0,1,1,1,0,-1)

N,M = map(int,input().split())
global clouds
clouds = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
global clouds_fields
cloud_fields = [[0 for i in range(N)] for j in range(N)]
for cloud in clouds:
    cloud_fields[cloud[0]][cloud[1]] = 1
global fields
fields = [list(map(int,input().split())) for _ in range(N)]
def Move(d,s):
    global cloud_fields
    nxt_clouds_fields = [[0 for i in range(N)] for j in range(N)]
    global clouds
    for cloud in clouds:
        cloud[0] += s*dy[d]
        cloud[1] += s*dx[d]
        if not 0 <= cloud[0] <= N-1:
            cloud[0] = cloud[0]%N
        if not 0 <= cloud[1] <= N-1:
            cloud[1] = cloud[1]%N
        nxt_clouds_fields[cloud[0]][cloud[1]] = 1
    cloud_fields = nxt_clouds_fields

def Water(coordinate):
    water = 0
    for i in [2,4,6,8]:
        y = coordinate[0] + dy[i]
        x = coordinate[1] + dx[i]
        if 0<=y<=N-1 and 0<=x<=N-1:
            if fields[y][x]:
                water += 1
    return water
def func():
    global clouds, fields, cloud_fields
    bugfields = []
    #구름에서 비가 내림
    for cloud in clouds:
        fields[cloud[0]][cloud[1]] += 1
    # 물복사가 일어날 지점과 일어날 양 
    for cloud in clouds:
        bugfields.append([cloud, Water(cloud)])
    # 물복사 버그 실행
    for bugfield in bugfields:
        y, x = bugfield[0]
        fields[y][x] += bugfield[1]
    # 구름과 물복사버그지대 초기화
    clouds.clear()
    bugfields.clear()
    nxt_clouds_fields = [[0 for i in range(N)] for j in range(N)]
    # 구름 재생성
    for i in range(N):
        for j in range(N):
            if cloud_fields[i][j]:
                continue
            if fields[i][j] >= 2:
                clouds.append([i,j])
                nxt_clouds_fields[i][j] = 1
                fields[i][j] -= 2
    cloud_fields = nxt_clouds_fields

for _ in range(M):
    d,s = map(int, input().split())
    Move(d,s)
    func()

water = 0
for i in range(N):
    for j in range(N):
        water += fields[i][j]
print(water)
