def solution(numbers):
    answer = []
    for number in numbers:
        f_number = 0
        bin_number = bin(number)
        if '0' not in bin_number[2:]:
            f_number = int('0b10'+bin_number[3:],2)
        else:
            i = len(bin_number)-1
            while True:
                if bin_number[i]=='0':
                    if i == len(bin_number)-1:
                        f_number = int(bin_number[:i]+'1'+bin_number[i+1:],2)
                    else:
                        f_number = int(bin_number[:i]+'10'+bin_number[i+2:],2)
                    break
                i -= 1
        answer.append(f_number)

    return answer

numbers = [2,5]

print(solution(numbers))