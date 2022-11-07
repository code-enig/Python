# 21C10 *50*7 ~1억:완전탐색(?)
# 가르칠수 있는 모든 글자의 조합을 구한뒤, 부분집합으로 구한다.
from itertools import combinations
import sys
sys.stdin = open('11th\\input','r')
N, K = map(int,sys.stdin.readline().split())
#필수로 알아야할 글자 a,n,t,i,c=> 5개
antic ={'a','n','t','i','c'}
wordset_list = [set(sys.stdin.readline().strip()[4:-4])-antic for _ in range(N)] # 필요한 알파벳이 담긴 set 리스트
max_count = 0

if K<5: # 배울수있는 글자가 5종류가 안되면 어떤 글자도 읽을 수 없다.
    print(0)
else:
    alphabets=set()
    for word in wordset_list:
        alphabets |= set(word) # 필요한 알파벳들만 고른다. antic 을 제외한 모든 글자인 21자 중에 택할 필요는 없다.

    if len(alphabets) < K-5:
        print(len(wordset_list)) #배울수 있는 글자 수가 배워야할 글자수 보다 많다면, 모든 글자를 배울 수 있으므로
    else:
        for alphabet_list in combinations(alphabets,K-5):
            test_set = set(alphabet_list)
            count = 0
            for wordset in wordset_list:
                if wordset <= test_set: # 부분집합인지 확인
                    count+=1
            if count > max_count:
                max_count = count
        print(max_count)