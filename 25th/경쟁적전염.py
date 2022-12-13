import sys
sys.stdin = open('Python\\25th\\input','r')
input = sys.stdin.readline
N,K = map(int,input().split())
viruses = [[] for _ in range(K+1)]
test_tube = [[-1 for _ in range(N+2)]]
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j]:
            viruses[tmp[j]].append((i+1,j+1))
    test_tube.append([-1]+tmp+[-1])
test_tube.append([-1 for _ in range(N+2)])
S,X,Y = map(int,input().split())

dr = [1,0,-1,0]
dc = [0,1,0,-1]
for _ in range(S):
    end_condition = True
    for i in range(1,len(viruses)):
        new_area = []
        while viruses[i]:
            t = viruses[i].pop()
            for k in range(4):
                r,c = t[0]+dr[k],t[1]+dc[k]
                if test_tube[r][c] == 0:
                    end_condition = False
                    test_tube[r][c] = i
                    new_area.append((r,c))
        viruses[i] = new_area
    if end_condition:
        break

print(test_tube[X][Y])    