# 루트 노드를 기준으로 작은 건 왼쪽 서브트리 큰 건 오른쪽 서브트리로 넣는다.
# 반복한뒤 왼->오->루 순으로 출력한다.
import sys
sys.setrecursionlimit(10000)
sys.stdin = open("Python\input",'r')
preorder_traverse_output = [int(k) for k in sys.stdin.readlines()] # 파이썬으로 입력제한이 없는 데이터를 받는 법

def postorder_traverse(start, end):
    if start > end: # 시작과 끝 위치가 뒤바뀌어 버리면 종료한다.(밑으로 노드가 더 이상 존재하지 않으면)
        return
    elif start == end:
        print(preorder_traverse_output[start])
        return

    nxt_end = end # 초기값, 아래쪽 for문이 돌아가지 않는 경우...
    for i in range(start+1, end+1):
        if preorder_traverse_output[i] > preorder_traverse_output[start]:
            nxt_end = i-1
            break
    postorder_traverse(start+1,nxt_end)  # 왼쪽 노드 출력
    postorder_traverse(nxt_end+1,end)        # 오른쪽 노드 출력
    print(preorder_traverse_output[start]) # 루트 노드 출력
    return


postorder_traverse(0,len(preorder_traverse_output)-1)