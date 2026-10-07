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


    