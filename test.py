stacks = [123,124]
giwon = 0
result= []
for stack in stacks:
    giwon = 0
    bonus = 0
    while stack+bonus < 200 and giwon <= 29:
        if 100<=stack+bonus<=105:
            bonus += 11
            giwon += 1
        elif 106<=stack+bonus<=111:
            bonus += 10
            giwon += 1
        elif 112<=stack+bonus<=119:
            bonus += 9
            giwon += 1
        elif 120<=stack+bonus<=129:
            bonus += 8
            giwon += 1
        elif 130<=stack+bonus<=144:
            bonus += 7
            giwon += 1
        elif 145<=stack+bonus<=158:
            bonus += 6
            giwon += 1
        elif 159<=stack+bonus<=185:
            bonus += 5
            giwon += 1
        elif 186<=stack+bonus<=208:
            bonus += 4
            giwon += 1
        elif 209<=stack+bonus<=227:
            bonus += 3
            giwon += 1
        elif 228==stack+bonus:
            bonus += 2
            giwon += 1
        elif 229==stack+bonus:
            bonus += 1
            giwon += 1

    result.append([stack,stack+bonus,giwon])
for line in result:
    print(line)