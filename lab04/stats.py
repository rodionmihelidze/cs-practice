def parse_record(line: str) -> dict:
    city, temp_raw, date = fields
    fields = line.split(";")
    if len(fields) != 3:
        raise ValueError("чего то не хватает")
    if not city or not date:
        raise ValueError(f"пустой город или дата: {line!r}")

    try:
        temperature = float(temp_raw)
    except ValueError:
        raise ValueError(f"температура не число: {temp_raw!r}")

    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if line.strip() == "":
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records

def count_errors(lines: list[str]) -> int:
    errors = 0
    for line in lines:
        if line.strip() == "":
            continue
        try:
            parse_record(line)
        except ValueError:
            errors += 1
    return errors

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for record in records:
        city = record["city"]
        total[city] = total.get(city, 0.0) + record["temperature"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}    