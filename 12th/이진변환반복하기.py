def solution(s):
    answer = []
    string = s
    num_zeros = string.count('0')
    rep = 0
    while True:
        number = string.count('1')
        string = str(bin(number))[2:]
        num_zeros += string.count('0')
        rep += 1
        if string == '1':
            answer = [rep, num_zeros]
            break
    return answer

print(solution("1111111"))