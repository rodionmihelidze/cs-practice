line = ' 2026-03-01T09:03:55 ERROR Не удалось открыть файл data.csv'

def parse_event(line):  
    b = line.split(maxsplit=2)
    level = ['DEBUG', 'INFO', 'WARNING', 'ERROR']
    print(b)
    print(len(b))
    k = {"time": '',
        "level": '',
        "message": ''}
    if len(b) == 2 or b[1] not in level:
        return ValueError
    else:
        k['level'] = b[1]
        k['time'] = b[0]
        k['message'] = b[2]
    return k

print(parse_event(line))