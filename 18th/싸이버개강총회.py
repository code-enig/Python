# 해싱
# 0~S: 입장, E~Q: 퇴장
# 입장 가능 시간에 채팅친 학생목록: 테이블 1, 퇴장 가능 시간에 채팅친 학생목록: 테이블 2
# 입장가능 시간에 채팅한 학생을 테이블1에 저장, 
# 퇴장가능 시간에 채팅한 학생을 테이블1, 테이블2 에서 검색, 테이블 1에 없으면 pass
# 테이블 2에도 있으면 pass, 테이블 2에는 없으면 count += 1, 테이블2 에 저장
import sys
sys.stdin = open('18th\\input','r')
input = sys.stdin.readline()

S,E,Q = [60*int(time.split(':')[0])+int(time.split(':')[1]) for time in input.split()] 
ent = dict()
ext = dict()
count = 0
inputs = sys.stdin.readlines()
for line in inputs:
    t, name = line.split()
    t = int(t.split(':')[0])*60 + int(t.split(':')[1])
    if t <= S:
        ent[name] = 1
    elif E <= t <= Q:
        try:
            if ent[name]:
                try:
                    if ext[name]:
                        pass
                except:
                    count += 1
                    ext[name] = 1
        except:
            pass
print(count)