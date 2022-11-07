# 분할해서 합치는 것이 아니라 합쳐서 통합한다. 역으로 연산
def solution(arr):
    answer = [0,0]
    # 종료 조건
    if len(arr) == 1:
        if arr[0][0] == 1 :
            return [0,1]
        elif arr[0][0] == 0:
            return [1,0]
        else: return [0,0]
    
    new_arr = [[-1 for i in range(len(arr)//2)] for j in range((len(arr)//2))]
    for y in range(0, len(arr)-1, 2):
        for x in range(0, len(arr)-1, 2):
            ones = 0
            zeros = 0
            uni = True
            for i in range(2):
                for j in range(2):
                    if arr[y+i][x+j] == -1:
                        uni = False
                        continue
                    if arr[y+i][x+j]:
                        ones += 1
                    else:
                        zeros += 1
            if not uni or (zeros != 4 and ones != 4): # 통합되어 있지 않을 때, 시작할 때는 모두 같은 숫자가 아닐때도 포함 
                answer[0] += zeros
                answer[1] += ones
            else:
                if ones == 4:
                    new_arr[y//2][x//2] = 1
                elif ones == 0:
                    new_arr[y//2][x//2] = 0
    zeros,ones = solution(new_arr)
    answer[0] += zeros
    answer[1] += ones
    
    return answer
    
arr = [[1,1],[1,1]]
print(solution(arr))