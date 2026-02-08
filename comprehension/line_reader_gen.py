import sys
from typing import Generator

# the reason the third argument is str is because the last line of the file is "This is the end of the file"
def read_line(file_path: str) -> Generator[str, None, str]:
    with open(file_path, 'r') as file:
        for line in file:
            yield line

    return "This is the end of the file"

def main() -> None:
    file_path: str = "data.txt"
    line_gen: Generator[str, None, str] = read_line(file_path)
    user_input: str = input('Tap "Enter" to start reading the file, or "q" to quit: ')
    
    while True:
        if user_input == "q":
            print("bye!")
            sys.exit(0)
        else:
            try:
                print(next(line_gen))
            except StopIteration as e:
                print("StopIteration error: ", e.value )
                sys.exit(0)
        user_input: str = input()

if __name__ == "__main__":
    main()