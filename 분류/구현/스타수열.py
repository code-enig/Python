# NN은 불가능
# SN 또는 NS 는 가능
# 그러나 NSN 은 불가능
# 원소 X의 좌우를 둘러보고 같은 값이 아닌 것과 짝을 짓는다. 짝을 지었다면 X와 다시 짝이 지어지면 안되므로 check 배열 값을 X로 바꾼다.

# (1, 0, 0, 1)
# ( 1,  1,  0,  0,  1,  1)
# (-1, -1,  1, -1, -1, -1)
def solution(a):
    answer = -1
    counter = [0 for _ in range(500000)]
    length = len(a)
    check = [-1 for _ in range(length+2)]
    a = [a[0]] + a + [a[-1]]
    for i in range(1,length+1):
        if a[i-1] != a[i] and check[i-1] != a[i]:
            check[i-1] = a[i]
            counter[a[i]] += 1
        elif a[i+1] != a[i] and check[i+1] != a[i]:
            check[i+1] = a[i]
            counter[a[i]] +=1
    answer = max(counter)*2
    return answer



a = [0,3,3,0,7,2,0,2,2,0]
print(solution(a))