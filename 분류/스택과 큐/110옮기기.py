def solution(s):
    answer = []
    for e in s:
        x=''
        if len(e) >= 3:
            stack = ''
            ooz = 0
            for oz in e:
                if len(stack) >= 2 and stack[-2:] == '11' and oz =='0':
                    ooz += 1
                    stack = stack[:-2]
                else:
                    stack = stack + oz
            if stack:
                for i,elem in enumerate(reversed(stack)):
                    if elem == '0':
                        x = stack[:len(stack)-i] +'110'*ooz+ stack[len(stack)-i:]
                        break
                else:
                    x = '110'*ooz + stack              
            else:
                x = '110'*ooz
        else:
            x = e
        answer.append(x) 
    return answer

s =  ["111100"]
print(solution(s))