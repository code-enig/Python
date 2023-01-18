import sys
sys.setrecursionlimit(1000000)
from itertools import product
def solution(clockHands):
    answer = float('inf')
    l_ark = len(clockHands)
    top_stats = list(product([0,1,2,3],repeat=l_ark))
    dr = [1,0,0]
    dc = [0,1,-1]
    copyHands = [[[-1,0] for _ in range(l_ark)] for _ in range(l_ark)]
    for n,stat in enumerate(top_stats):
        tot_rot_num = 0
        for col in range(l_ark):
            if stat[col]:
                tot_rot_num += stat[col]
                if copyHands[0][col][0] != n:
                    copyHands[0][col] = [n,(clockHands[0][col] + stat[col])%4]
                else:
                    copyHands[0][col][1] = (copyHands[0][col][1] + stat[col])%4
                for i in [0,1,2]:
                    nxt_row = dr[i]
                    nxt_col = col + dc[i]
                    if 0 <= nxt_row < l_ark and 0 <= nxt_col < l_ark:
                        if copyHands[nxt_row][nxt_col][0] != n:
                            copyHands[nxt_row][nxt_col] = [n,(clockHands[nxt_row][nxt_col] + stat[col])%4]
                        else:
                            copyHands[nxt_row][nxt_col][1] = (copyHands[nxt_row][nxt_col][1] + stat[col])%4  
        for row in range(1, l_ark):
            for col in range(l_ark):
                if copyHands[row-1][col][0] != n:
                    rot_num = (4 - clockHands[row-1][col])%4
                else:
                    rot_num = (4 - copyHands[row-1][col][1])%4
                copyHands[row-1][col] = [n,0]
                if rot_num:
                    tot_rot_num += rot_num
                    if copyHands[row][col][0] != n:
                        copyHands[row][col] = [n,(clockHands[row][col]+ rot_num)%4]
                    else:
                        copyHands[row][col][1] = (copyHands[row][col][1] + rot_num)%4    
                    for i in [0,1,2]:
                        nxt_row = row + dr[i]
                        nxt_col = col + dc[i]
                        if 0 <= nxt_row < l_ark and 0 <= nxt_col < l_ark:
                            if copyHands[nxt_row][nxt_col][0] != n:
                                copyHands[nxt_row][nxt_col] = [n,(clockHands[nxt_row][nxt_col] + rot_num)%4]
                            else:
                                copyHands[nxt_row][nxt_col][1] = (copyHands[nxt_row][nxt_col][1] + rot_num)%4
        if sum([copyHands[-1][i][1] for i in range(l_ark)]) == 0:
            answer = min(answer,tot_rot_num)
    return answer


print(solution([[0, 1, 3, 0],
[1, 2, 0, 0],
[3, 0, 2, 2],
[0, 2, 0, 0]]))