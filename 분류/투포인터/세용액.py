# 두용액 응용 양 끝에서 투포인터로 용액 특성값의 합을 계속 구해오면서, 이분탐색으로 그 특성값의 합과 부호가 반대이고 절댓값이 같은 특성치에 가장 가까운 용액을 찾아서 섞는다.
import sys
import bisect
N = int(sys.stdin.readline())
INF = float('inf')

def threesols(ss):
    three_sols = []
    solutions = ss
    min_ch_val_sum= INF
    lv_ind = bisect.bisect_left(solutions, 0)-1
    for i in range(0, 3):
        try:
            tmp_val = solutions[lv_ind+(i-2)]+solutions[lv_ind+(i-1)]+solutions[lv_ind+i]
            if abs(tmp_val) < min_ch_val_sum :
                min_ch_val_sum = abs(tmp_val)
                three_sols = [solutions[lv_ind+(i-2)],solutions[lv_ind+(i-1)],solutions[lv_ind+i]]
        except IndexError:
            pass            
    return three_sols, min_ch_val_sum

solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()
three_solutions, min_ch_val_sum = threesols(solutions)

left_start = 0
left_end = min(bisect.bisect_right(solutions, 0), len(solutions)-3)
for j in range(left_start, left_end+1):
    right_end = max(bisect.bisect_left(solutions, -solutions[j]//2)-1, j + 2)
    right_start = len((solutions))-1
    for i in range(right_start,right_end-1,-1):
        tmp_sum = solutions[j] + solutions[i]
        sol3_ind = (i+j)//2
        left_index = bisect.bisect_left(solutions, -tmp_sum)-1
        right_index =  bisect.bisect_left(solutions, -tmp_sum)
        
        if right_index <= j:
            right_index = j+1
        elif right_index >= i:
            right_index = i-1
        
        if left_index <= j:
            left_index = j+1
        elif left_index >=i:
            left_index = i-1  
        if abs(tmp_sum + solutions[left_index]) > abs(tmp_sum + solutions[right_index]):
            sol3_ind = right_index
        else:
            sol3_ind = left_index
        tmp_sum += solutions[sol3_ind] 
        if abs(tmp_sum) < min_ch_val_sum:
            min_ch_val_sum = abs(tmp_sum)
            three_solutions = [solutions[j],solutions[sol3_ind],solutions[i]]
        if min_ch_val_sum == 0:
            break
for solution in three_solutions:
    print(solution, end = ' ')