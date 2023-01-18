# 완전 탐색 자릿수가9자리 이므로 올라가든 내려가든 2경우로 2^9~512가지 경우 뿐이 없다.
def solution(storey):
    answer = 100
    n = 1
    while True:
        q = storey//(10**n)
        r = storey%(10**n)
        if r != 0:
            r_n = int(str(r)[0])
            answer = min(solution(storey-r)+r_n,solution(storey+10**(n)-r)+10-r_n)
        else:
            if 1 <= q <= 9: 
                return min(q, 11-q)
            else:
                n += 1
                continue  
        break
    return answer
print(solution(9191))
