with open(input(), encoding='utf-8') as file:
    res = []
    last_line = ' '
    for line in file:
        if line.startswith('def') and not last_line.startswith('#'):
            res.append(line[4:line.find('(')])
        last_line = line

if len(res):
    print(*res, sep='\n')
else:
    print('Best Programming Team')