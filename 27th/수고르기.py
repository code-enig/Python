# 두 수 차이의 경우의 수 = (10^5)^2 >> 10^9 시간초과
# 중복되는 a[i]가 없다고 가정한다.
# 수들을 정렬한다 -> A[j]-A[i] < M 인 경우 j++ 
# 이상이면 i++, 근데 이 때 j 값을 초기화 할 필요는 없다.
# 현재 j 보다 작은 j 에서 A[j]-A[i++] >= M 인 경우는 있을 수는 없기 때문에
# A[j]-A[i] > A[j]-A[i++] > A[j--]-A[i++] 이므로   
import sys
sys.stdin = open('Python\\input','r')
N,M= map(int,sys.stdin.readline().split())
numbers = set()
for _ in range(N):
    numbers.add(int(sys.stdin.readline()))
numbers = list(numbers)
numbers.sort()
answer = numbers[-1] - numbers[0]
right = 0
for small in numbers:
    while right < len(numbers):
        big = numbers[right]
        if big - small >= M:
            answer = min(answer, big - small)
            break
        right += 1
    if answer == M:
        break

print(answer)