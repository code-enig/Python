# 시작일이 같을 경우 일정의 기간이 긴 것이 먼저 채워진다.
import sys
sys.stdin = open('Python\\input','r')
N= int(sys.stdin.readline())
schs = []
for _ in range(N):
    schs.append(list(map(int,sys.stdin.readline().split())))
schs.sort(key = lambda x: x[0])
answer = 0
width = 1
start,end = schs[0]
ends = [end]

for i in range(1,len(schs)):
    nxt_start, nxt_end = schs[i]

    if nxt_start > end+1:
        answer += width*(end-start+1)
        start, end = nxt_start, nxt_end
        ends = [end]
        width = 1
        continue

    for j in range(len(ends)):
        if nxt_start > ends[j]:
            ends[j] = nxt_end
            end = nxt_end if nxt_end > end else end
            break
    else:
        width += 1
        ends.append(nxt_end)
        end = nxt_end if nxt_end > end else end
else:
    answer += width*(end-start+1)

print(answer)