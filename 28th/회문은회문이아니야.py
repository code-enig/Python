import sys
sys.stdin = open('Python\\input','r')
string = sys.stdin.readline().rstrip()
length = len(string)
test_length = length//2
if string[:test_length] != string[length:length-test_length-1:-1]:
    print(length)
else:
    if string.count(string[0]) != length:
        print(length-1)
    else:
        print(-1)