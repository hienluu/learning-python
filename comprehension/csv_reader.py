import csv, sys
from typing import Generator

def read_csv(file_path: str) -> Generator[list[str], None, None]:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row

def main() -> None:
    file_path: str = "csv_data.txt"
    csv_gen: Generator[list[str], None, None] = read_csv(file_path)

    while True:
        try:
            for _ in range(3):
                print(next(csv_gen))
        except StopIteration as e:
            print("Now more row!! ", e.value )
            sys.exit(0)
        user_input: str = input('Tap "Enter" to continue, or "q" to quit: ')
        if user_input == "q":
            print("bye!")
            sys.exit(0)
        else:
            continue

if __name__ == "__main__":
    main()