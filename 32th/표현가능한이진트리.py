# 포화 이진트리의 노드 갯수 : 2^k - 1, k는 트리의 높이
# 만약 어떤수의 이진수표현 자릿수가 높이 k인 트리 의 노드 갯수보다 적은데도 표현을 못하는 경우에, 
# 트리의 높이가 더 높아지면 표현이 가능해질 수도 있는가?
# -> 불가능하다.
# 더미 노드 아래로는 다 더미 노드
# 포화 이진트리 탐색 방법: ???
# 루트 노드 번호: (2**(k-1) - 1) + 1 = 2**(k-1)
# 트리문제가 아니네 ㅋㅋㅋ
def solution(numbers):
    answer = []
    for number in numbers:
        b_num = format(number, 'b')
        b_digit = len(str(b_num))
        k = 0
        while True:
            if 2**k -1 >= b_digit:
                break
            k += 1
        str_b_num = ''.join(['0' for _ in range((2**k - (1+b_digit)))]) + str(b_num)
        dummy = True if str_b_num[2**(k-1)-1] == '0' else False
        answer.append(can_present(str_b_num,2**(k-1)-1,dummy)) # index는 0 부터 시작
        
    return answer
def can_present(str_b_n,mid,dummy):
    if len(str_b_n) == 1:
        if dummy and (str_b_n[mid] == '1'):
            return 0
        else :
            return 1
    if dummy and str_b_n[mid] =='1':
        return 0
    else:
        nxt_dummy = True if str_b_n[mid] == '0' else False
        return can_present(str_b_n[:mid],(mid-1)//2,nxt_dummy) and can_present(str_b_n[mid+1:],(mid-1)//2,nxt_dummy)
    
print(solution([63, 111, 95]))