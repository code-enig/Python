from sys import stdin
stdin = open('input','r')
n = int(stdin.readline())
case = [False for _ in range(0,26)]

for _ in range(n):
    words = list(stdin.readline().split())
    output_words =[]
    flag = False
    for word in words:
        if not flag:
            if ord(word[0])<97 and not case[ord(word[0])-65]: 
            # 아직 단축키를 찾지 못했고 첫글자가 단축키로 지정되지 않았을 때
                output_words.append("".join(['[', word[0], ']',word[1:]]))
                case[ord(word[0])-65] = True
                flag = True # 단축키를 찾았음을 표지
            elif ord(word[0]) >= 97 and not case[ord(word[0])-97]:      
                output_words.append("".join(['[', word[0], ']',word[1:]]))
                case[ord(word[0])-97] = True
                flag = True # 단축키를 찾았음을 표지
            else:
                output_words.append(word)            
        else:
            output_words.append(word)
    if flag:
        print(" ".join(output_words))
    else:
        output_words = []      
        for word in words:
            if not flag:
                sc_word = ''
                for ab in word:
                    if not flag and ord(ab[0])<97 and not case[ord(ab[0])-65]: 
                    # 아직 단축키를 찾지 못했고 이 글자가 단축키로 지정되지 않았을 때
                        sc_word = "".join([sc_word, '[', ab, ']'])
                        case[ord(ab)-65] = True
                        flag = True # 단축키를 찾았음을 표지
                    elif not flag and ord(ab) >= 97 and not case[ord(ab)-97]:      
                        sc_word = "".join([sc_word, '[', ab, ']'])
                        case[ord(ab)-97] = True
                        flag = True # 단축키를 찾았음을 표지
                    else:
                        sc_word = "".join([sc_word, ab])
                output_words.append(sc_word)     
            else:
                output_words.append(word)
        print(" ".join(output_words))