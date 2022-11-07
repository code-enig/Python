# 메모리 초과
# 1. 자원 카드 n을 획득한 사람이 다시 acquire n을 수행하는 경우는 주어지지 않습니다.
# 2. 획득하지 않은 자원 카드를 release 하는 경우는 주어지지 않습니다.
# => T턴동안 T번 실행된다.
import sys
sys.stdin = open('23th\\input','r')
input = sys.stdin.readline
N,T = map(int,input().split())
turn = list(map(int,input().split()))
card_dummy = [list(input().split()) for _ in range(T)]
acquire_set = set([]) # 누가 가져갔는지 알려줄 set
own_card = [[] for _ in range(N+1)] # 연산카드 대기열
card_number = 0
for man_number in turn:
    # 카드를 가지고 있는 경우
    if own_card[man_number]:
        r, id = own_card[man_number]
        print(id)
        if r not in acquire_set:
            acquire_set.add(r)
            own_card[man_number].clear()
        continue
    # 소유한 카드가 없을 경우
    op_card = card_dummy[card_number]
    card_number += 1 # 더미에 있는 카드를 꺼낸다
    id = int(op_card[0])
    kind = op_card[1] 
    if kind == 'next' :
        print(id)
        continue
    if kind == 'acquire':
        r = int(op_card[2])
        if r in acquire_set:
            own_card[man_number] = [r,id] # 손에 든 패는 1장까지 가능하다.
            print(id)
        else:
            acquire_set.add(r) 
            print(id)
    else:
        r = int(op_card[2])
        acquire_set.remove(r) # 조건 2에 의해 오류 안남.
        print(id)
