import sys

from gradebook.core import load_records
from gradebook.report import format_report


def main(argv):
    path = argv[1] if len(argv) > 1 else "data/grades.csv"
    try:
        records = load_records(path)
    except (OSError, ValueError, KeyError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(format_report(records))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
