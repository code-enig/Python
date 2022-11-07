# 설치된 레이저 위로 몇마리 넴모가 있는가?가 핵심
# BS로 설치된 레이저 위치(x,y)보다 작은수(<x)가 나오는걸 찾기
# 특정 값보다 작은 값중에 가장 큰 값이나 큰 값중 가장 작은 값 찾는 BS, 이 경우는 큰 값중 가장 작은 값 => max를 계속 줄이다가 조건을 만족하지 않는 순간의 전 값을 취하면 된다.
import sys
sys.stdin = open('18th\\input', 'r')
input = sys.stdin.readline

N, Q = map(int, input().split())
nemmo = list(map(int, input().split()))
for _ in range(Q):
    x, y = map(int, input().split())
    answer = max(nemmo[y-1]-x+1, 0)
    if not answer: # 중력에 의해 오른쪽에 넴모가 없다면, 위로도 없다.
        print(answer)
    else:
        mn, mx = y-1, N-1
        while mn <= mx:
            mid = (mn+mx)//2
            if nemmo[mid] >= x:
                mn = mid + 1
            else:
                mx = mid - 1
        print(answer + mx+1-y)
