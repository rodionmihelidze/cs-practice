import logstats


def main():
    path = input().strip()

    with open(path, encoding="utf-8") as log:
        counts = logstats.count_levels(log)

    with open(path, encoding="utf-8") as log:
        errors = logstats.top_errors(log, 3)

    total = 0
    for key in counts:
        total = total + counts[key]

    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total)
    print(error_count)
    print(broken_count)

    report = logstats.format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(report)


if __name__ == "__main__":
    main()