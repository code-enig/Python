# BFS, DFS 둘다 가능할 거 같음
# 사실 둘다 아니었음
import sys
sys.stdin = open('23th\\input','r')
input = sys.stdin.readline

N = int(input())
final_colors = tuple(map(int,input().split())) # 트리 최종 목표 색상
times = 1 if final_colors[0] else 0 # 처음에 색을 칠하고 시작하느냐 아니냐
for _ in range(N-1):
    n1,n2 = map(int,input().split())
    # 만약 서로 연결된 노드 끼리 원하는 색상이 다르다면 아랫 노드에 무조건 한번씩 덧칠해야한다.
    # 만약 같다면 아랫 노드 색칠하는걸 건너 뛰어도 된다.
    times += 1 if final_colors[n1-1] != final_colors[n2-1] else 0
print(times)