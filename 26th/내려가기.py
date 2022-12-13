# 3칸에 그 칸으로 끝났을때 가질수 있는 최댓값,최솟값을 갱신해가면서 DP로 풀면 될것 같다.
import sys
sys.stdin = open('Python\\26th\\input','r')
input = sys.stdin.readline
N = int(input())

dp_max = [0 for _ in range(3)]
dp_min = [0 for _ in range(3)]
for _ in range(N):
    n1, n2, n3 = map(int, input().split())
    dp_max1, dp_max2, dp_max3 = dp_max[0],dp_max[1],dp_max[2]
    dp_min1, dp_min2, dp_min3 = dp_min[0],dp_min[1],dp_min[2]
    dp_max[0], dp_max[1], dp_max[2] = n1 + max(dp_max1, dp_max2), n2 + max(dp_max1, dp_max2, dp_max3), n3 + max(dp_max2, dp_max3)
    dp_min[0], dp_min[1], dp_min[2] = n1 + min(dp_min1, dp_min2), n2 + min(dp_min1, dp_min2, dp_min3), n3 + min(dp_min2, dp_min3)

print(max(dp_max), min(dp_min))