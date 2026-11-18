from pstats import SortKey


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

LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]


def parse_event(line):
    parts = line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("слишком мало частей в строке")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError("незнакомый уровень: " + level)
    return {"time": time, "level": level, "message": message}


def count_levels(lines):
    counts = {}
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        try:
            event = parse_event(line)
        except ValueError:
            key = "BROKEN"
        else:
            key = event["level"]
        if key in counts:
            counts[key] = counts[key] + 1
        else:
            counts[key] = 1
    return counts


def top_errors(lines, n):
    messages = {}
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] != "ERROR":
            continue
        msg = event["message"]
        if msg in messages:
            messages[msg] = messages[msg] + 1
        else:
            messages[msg] = 1
    pairs = []
    for msg in messages:
        pairs.append([msg, messages[msg]])
        return (-pairs[1], pairs[0])

    pairs.sort(key=SortKey)
    result = []
    for i in range(len(pairs)):
        if i >= n:
            break
        result.append(pairs[i])
    return result


def format_report(counts, errors):
    text = "Отчёт по журналу\n\n"
    keys = []
    for key in counts:
        keys.append(key)
    keys.sort()
    for key in keys:
        text = text + key + ": " + str(counts[key]) + "\n"

    text = text + "\nЧастые ошибки:\n"
    for pair in errors:
        text = text + "- " + pair[0] + " — " + str(pair[1]) + "\n"

    return text