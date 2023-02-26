# 정렬
import sys
sys.stdin = open('Python\\input','r')
row,col = map(int, sys.stdin.readline().split())
board = []
for _ in range(row):
    tmp = sys.stdin.readline().rstrip()
    tmp_line =[]
    for character in tmp:
        tmp_line.append(character)
    board.append(tmp_line)

def find_words(board):
    words_list = []
    for line in board:
        word = []
        for ch in line:
            if ch != '#':
                word.append(ch)
                continue
            if len(word) >= 2:
                words_list.append(word)
            word =[]
        else:
            if len(word) >= 2:
                words_list.append(word)      
    return words_list

def first_dic(words_list):
    first_word = ['z' for _ in range(max(row,col))]
    for word in words_list:
        for i in range(min(len(first_word),len(word))):
            if ord(word[i]) > ord(first_word[i]):
                break
            if ord(word[i]) < ord(first_word[i]): # 적어도 같은 사전 순임이 보장 된다.
                first_word = word
                break
        else:
            if len(word)< len(first_word):
                first_word = word
    return ''.join(first_word)

def sol():
    answer_list = []
    answer_list.extend(find_words(board))
    col_board = [[board[i][j] for i in range(row)] for j in range(col)]
    answer_list.extend(find_words(col_board))
    print(first_dic(answer_list))

sol()