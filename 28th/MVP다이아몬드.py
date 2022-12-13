import sys
sys.stdin = open('Python\\input','r')
N = int(sys.stdin.readline())
std = list(map(int,sys.stdin.readline().split()))
grades = sys.stdin.readline().rstrip()

def max_waste(money,grade,nxt_grade):
    if grade == 'B':
        tmp_waste = std[0] - money - 1
    elif grade == 'S':
        tmp_waste = std[1] - money - 1
    elif grade == 'G':
        tmp_waste = std[2] - money - 1
    elif grade == 'P':
        tmp_waste = std[3] - money - 1
    else:
        tmp_waste = std[3]

    if nxt_grade == 'B':
        return min(std[0]-1,tmp_waste)
    elif nxt_grade == 'S':
        return min(std[1]-1,tmp_waste)
    elif nxt_grade == 'G':
        return min(std[2]-1,tmp_waste)
    elif nxt_grade == 'P':
        return min(std[3]-1,tmp_waste)
    else:
        return tmp_waste

tot_waste = 0
prv_waste = 0
for i in range(N-1):
    waste = max_waste(prv_waste,grades[i],grades[i+1])
    tot_waste += waste
    prv_waste = waste
tot_waste += max_waste(prv_waste,grades[i+1],'D')

print(tot_waste)
