LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]


def parse_event(line):
    line = line.strip()
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

    def sort_key(pair):
        return (-pair[1], pair[0])

    pairs.sort(key=sort_key)

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