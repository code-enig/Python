# 구현
# n^2 ~ 10^14: 에니메이션처럼 하면 시간초과
# 행렬 요소를 (j,k) 라고 하면
# left = j*n + k, j = left//n, k = left%n
# right = j*n + k + left
# j 번째 행 : j가 j개, j+1,j+2...n
# left(j행 k열):  j if j>=k else k

def solution(n, left, right):
    answer = []
    row = left // n # 몇번째 행
    column = left % n # 나누어 떨어지면 마지막
    length = right - left + 1
    if length <= n - column: # 시작 행보다 짧거나 같을 때
        answer = [row+1 if i <= row else i+1 for i in range(column,column+length)]
    elif  length <= 2*n - column: #다음 행에서 끝날 때
        answer = [row+1 if i <= row else i+1 for i in range(column,n)]
        answer.extend([row+2 if i <= row+1 else i+1 for i in range(0,length-(n-column))])
    else:
        answer = [row+1 if i <= row else i+1 for i in range(column,n)]
        num_rows = 0
        for row in range(row+1, row+1+(length-(n-column))//n):
            num_rows += 1
            answer.extend([row+1 if i <= row else i+1 for i in range(0,n)])
        row+=1
        answer.extend([row+1 if i <= row else i+1 for i in range(0,length-(n-column)-n*num_rows)])
    
    return answer

print([1,2,3])
print([2,2,3])
print([3,3,3])
print()

n, left, right = 3, 3, 5

print(solution(n,left,right))