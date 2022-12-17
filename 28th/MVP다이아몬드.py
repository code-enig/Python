import sys
N = int(sys.stdin.readline())
global std
std = list(map(int,sys.stdin.readline().split()))
grades = sys.stdin.readline().rstrip()

def max_waste(money,grade):
    global std
    if grade == 'B':
        return std[0] - money - 1
    elif grade == 'S':
        return std[1] - money - 1
    elif grade == 'G':
        return std[2] - money - 1
    elif grade == 'P':
        return std[3] - money - 1
    else:
        return std[3]

tot_waste = 0
prev_waste = 0

for grade in grades:
    waste = max_waste(prev_waste,grade)
    tot_waste += waste
    prev_waste = waste
print(tot_waste)