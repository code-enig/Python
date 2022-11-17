def solution(k, ranges):
    answer = []
    input = k
    seq = [input]
    while input != 1:
        if input%2:
            seq.append(input*3+1)
            input = input*3 + 1
        else:
            seq.append(input//2)
            input = input//2
    for start,end in ranges:
        if start > len(seq) + end - 1:
            answer.append(-1.0)
        else:
            temp = 0
            for x in range(start,len(seq)+end-1):
                temp += (seq[x]+seq[x+1])/2
            answer.append(float(temp))
    return answer


k, ranges = 5,[[0,0],[0,-1],[2,-3],[3,-3]]

print(solution(k,ranges))