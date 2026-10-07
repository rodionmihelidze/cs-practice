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



    