# ?? set?
import sys
sys.stdin = open('input','r')
n = int(sys.stdin.readline())
prefix_set = set()
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    flag = True # 이 단어를 집합에 넣을지 말지 정할 지표
    length = 0
    if word in prefix_set:
        continue
    tmp_word = None
    for comp_word in prefix_set:
        if len(word)>len(comp_word): # 8줄에서 같은 단어는 배제 하였다.
            length = len(comp_word)
        else:
            length = len(word)
            flag = False
        for i in range(length):
            if word[i] != comp_word[i]:
                flag = True # 접두어가 아니다. 따라서 넣는다.
                break
        else:
            tmp_word = comp_word
            break
    if flag: # 만약 처음에 단어가 하나도 없어서 비교를 못했을 경우.flag 초기값이 True 이므로 그냥 담는다.
        prefix_set.add(word) 
        if tmp_word:
            prefix_set.remove(tmp_word)

print(len(prefix_set))