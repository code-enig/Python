# 메모리 초과
# 1. 자원 카드 n을 획득한 사람이 다시 acquire n을 수행하는 경우는 주어지지 않습니다.
# 2. 획득하지 않은 자원 카드를 release 하는 경우는 주어지지 않습니다.
# => T턴동안 T번 실행된다, 조건에 명시된 행동만 할 수 있게 주어진다.
import sys
sys.stdin = open('23th\\input','r')
input = sys.stdin.readline
N,T = map(int,input().split())
turn = list(map(int,input().split()))
card_dummy = [list(input().split()) for _ in range(T)]
acquire_set = set([]) # 누군가 이미 가져갔는지 알려줄 set
own_card = [[] for _ in range(N+1)] # 연산카드 대기열
card_number = 0
for man_number in turn:
    # 카드를 가지고 있는 경우
    if own_card[man_number]:
        r, id = own_card[man_number]
        print(id) # 카드 번호를 출력한다.
        if r not in acquire_set: # 누군가 가져가지 않았다면
            acquire_set.add(r) # 가져가고
            own_card[man_number].clear() # 연산카드를 버린다.
        continue
    # 소유한 카드가 없을 경우
    op_card = card_dummy[card_number]
    card_number += 1 # 더미에 있는 카드를 꺼낸다
    id = int(op_card[0])
    card_type = op_card[1] 
    if card_type == 'next' :
        print(id)
        continue
    if card_type == 'acquire':
        r = int(op_card[2])
        if r in acquire_set: # 누군가 가져갔다면
            own_card[man_number] = [r,id] # 패를 간직한다.
            print(id)
        else:
            acquire_set.add(r) # 아니라면 자원을 가져간다.
            print(id)
    else:
        r = int(op_card[2])
        acquire_set.remove(r) # 자원을 버린다. 조건 2에 의해 오류 안남.
        print(id)
