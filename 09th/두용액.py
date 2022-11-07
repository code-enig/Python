# 투포인터
import sys
N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))

ac_sum = 2000000001
acids = []
bases = []
solutions.sort()
for i, solution in enumerate(solutions):
    if solution > 0:
        bases = solutions[:i]
        acids = solutions[i:]
        break
else:
    bases = solutions
base_num = 0
acid_num = len(acids)-1

if not acids:
    print(bases[-2],bases[-1])
    sys.exit(0)
if not bases:
    print(acids[0],acids[1])
    sys.exit(0)
i , j = 0, len(acids)-1
for i in range(len(bases)):
    while j >= 0:
        if abs(bases[i] + acids[j]) < ac_sum:
            base_num, acid_num, ac_sum = i, j, abs(bases[i] + acids[j])
        if abs(bases[i]) > abs(acids[j]):
            break
        if ac_sum == 0:
            break    
        j -= 1
    if ac_sum == 0:
        break

if len(bases) > 1 and abs(bases[-2]+bases[-1]) < ac_sum:
    print(bases[-2],bases[-1])
elif len(acids) > 1 and abs(acids[0]+acids[1]) < ac_sum:
    print(acids[0], acids[1])
else:
    print(bases[base_num], acids[acid_num])