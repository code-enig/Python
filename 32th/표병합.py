#귀찮음 딕셔너리 이용해서 병합을 표현
table = [[None for _ in range(51)] for _ in range(51)]
merged_cells = {}
for i in range(1,51):
    for j in range(1,51):
        merged_cells[(i,j)] = [(i,j)]
def solution(commands):
    answer = []
    for command in commands:
        inputs = list(command.split())
        if inputs[0] == "UPDATE":
            if len(inputs) == 4:
                func1(inputs[1],inputs[2],inputs[3])
            else:
                func2(inputs[1],inputs[2])
        elif inputs[0] == "MERGE":
            func3(inputs[1],inputs[2],inputs[3],inputs[4])
        elif inputs[0] == "UNMERGE":
            func4(inputs[1],inputs[2])
        else:
            answer.append(func5(inputs[1],inputs[2]))
    return answer

def func1(s1,s2,s3):
    r,c = map(int, [s1, s2])
    for mr,mc in merged_cells[(r,c)]:
        table[mr][mc] = s3
    return

def func2(s1,s2):
    for i in range(1,51):
        for j in range(1,51):
            if table[i][j] == s1:
                table[i][j] = s2
    return

def func3(s1,s2,s3,s4):
    r1,c1,r2,c2 = map(int, [s1,s2,s3,s4])
    if (r1,c1) in merged_cells[(r2,c2)]:
        return
    value = None
    if table[r1][c1]:
        value = table[r1][c1]
    elif not table[r1][c1] and table[r2][c2]:
        value = table[r2][c2]
    tmp_merged_cell_list = []
    tmp_merged_cell_list.append((r1,c1))
    tmp_merged_cell_list.append((r2,c2))
    tmp_merged_cell_list.extend(merged_cells[(r1,c1)])
    tmp_merged_cell_list.extend(merged_cells[(r2,c2)])
    for r,c in tmp_merged_cell_list:
        table[r][c] = value
        merged_cells[(r,c)] = tmp_merged_cell_list
    return
    
def func4(s1,s2):
    r, c = map (int, [s1, s2])
    value = table[r][c]
    unmerged_list = merged_cells[(r,c)]
    for ur,uc in unmerged_list:
        table[ur][uc] = None
        merged_cells[(ur,uc)] = [(ur,uc)]
    table[r][c] = value
    return
        
def func5(s1,s2):
    r,c = map(int, [s1,s2])
    return table[r][c] if table[r][c] else "EMPTY"

commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
print(solution(commands))
commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
print(solution(commands))