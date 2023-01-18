# l, r이 11011 영역에 있는가, 00000 영역에 있는가,? 있다면 어디에 있는가?
# 5^n 개의 숫자를 가지고 있다고 생각 하니씩 펼치면서, l,r의 위치를 찾는다.
# ex) 2,4,17의 경우=> 5^2개의 숫자를 품고 있다고 생각 처음 펼치면 abcde 이중 4 의 위치는 a에 17의 위치는 d에 위치한다.
# 이제 a를 다시 a'b'c'd'e'로 쪼개면 4의 위치는 d', 마찬가지로 17의 위치는 b' 이다.
# bc는 포함이므로 b=1 c= 0 였으므로, 합계 1 4개
# a의 d'위치에서 110'1'1 에서 11 2개
# d의 b'위치에서 1'1'011 에서 11 2개
# 총 8개이다.
# l-1과 r-1을 5진수로 바꾼다. (0~5^n-1 까지 총 5^n 개의 영역에 위치를 가리키도록, 그냥하면, 인덱스가 한칸씩 밀려 귀찮으므로...)

def solution(n, l, r):
    answer = 4**n #원래 1의 총 갯수
    ql = quinary(l,n+1)
    qr = quinary(r,n+1)
    for i in range(1,n+1):
        answer -= '11011'[0:ql[i]].count('1')*(4**(n-i)) # 이만큼의 1은 앞에서 빠진다.
        if ql[i] == 2: # 한번 0 영역으로 들어오면 무조건 0 이고 더 이상의 1은 없다.
            break
    for j in range(1,n+1):
        answer -= '11011'[qr[j]+1:].count('1')*(4**(n-j)) # 이만큼의 1은 뒤에서 빠진다.
        if qr[j] == 2 :
            break
    return answer

def quinary(number,length): # 어떤 수 -1 을 거꾸로 된 5진수로 반환해주는 함수 모자라는 자리는 0 으로 채워서 반환
    n = number-1
    ret = []
    while True:
        if n//5 == 0:
            ret.append(n%5)
            break
        else:
            ret.append(n%5)
            n = n//5
    ret = ret +[0 for _ in range(length-len(ret))]
    return list(reversed(ret))
 
print(solution(2,4,17))
