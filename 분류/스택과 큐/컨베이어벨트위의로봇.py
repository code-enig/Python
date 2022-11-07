#시키는대로
import sys
from collections import deque
def StepOne():
    global belt, robots
    belt.rotate(1)
    robots.rotate(1)
    robots[0] = 0
    robots[-1] = 0

def StepTwo():
    global belt, robots, count
    for i in range(N-2,-1,-1):
        if robots[i] and not robots[i+1] and belt[i+1] > 0:   
            robots[i] = 0
            belt[i+1] -= 1
            if belt[i+1] == 0:
                count += 1
            if i == N-2:
                continue
            robots[i+1] = 1
            
def StepThree():
    global belt, robots, count
    if belt[0] > 0:
        belt[0] -= 1
        robots[0] = 1
        if belt[0] == 0:
            count += 1

sys.stdin = open('17th\\input', 'r')
input = sys.stdin.readline
N,K = map(int, input().split())
global belt,robots,count
belt = deque(list(map(int,input().split())))
robots = deque([0 for _ in range(N)])
count = 0
step = 0
while True:
    step += 1
    StepOne()
    StepTwo()
    if count >= K:
        print(step)
        sys.exit(0)
    StepThree()
    if count >= K:
        print(step)
        sys.exit(0)
