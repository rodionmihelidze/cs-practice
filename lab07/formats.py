import json
def csv_to_records(text):
    if not text or not text.strip():
        return []

    lines = text.splitlines()
    if not lines:
        return []

    header = [col.strip() for col in lines[0].split(",")]
    records = []

    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        record = {}
        for i, col in enumerate(header):
            record[col] = values[i] if i < len(values) else ""
        records.append(record)

    return records


def _parse_scalar(value: str):
    value = value.strip()
    if value == "":
        return ""

    lower = value.lower()

    if lower in ("true", "yes"):
        return True
    if lower in ("false", "no"):
        return False

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value
