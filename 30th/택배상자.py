#stack? 구현?
def solution(order):
    answer = 0
    sub = [i for i in range(1,order[0])]
    main = [j for j in range(len(order),order[0]-1,-1)]
    print(main,sub)
    while answer <= len(order):   
        if main and order[answer] == main[-1]:
            main.pop()
            answer += 1
        elif sub and order[answer] == sub[-1]:
            sub.pop()
            answer += 1
        elif main:
            sub.append(main.pop())
        else:
            break
    return answer

order=[2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

print(solution(order))