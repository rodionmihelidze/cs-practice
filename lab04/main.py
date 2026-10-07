import sys
from stats import average_by_city, read_valid, warmest_city, count_errors
def main() -> None:
    lines = sys.stdin.read().splitlines()

    records = read_valid(lines)
    errors = count_errors(lines)

    print(len(records))
    print(errors)

    best = warmest_city(records)
    if best == "":
        print("0.0")
    else:
        print(f"{average_by_city(records)[best]:.1f}")

if __name__ == "__main__":
    main()
    