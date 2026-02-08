from typing import Generator, Any

# this repeater repeats the sequence indefinitely due to the while True loop
# onces it reaches the end of the sequence, it starts over from the beginning
def repeater(sequence: list[Any]) -> Generator[Any, None, None]:
    while True:
        for item in sequence:
            yield item

def main() -> None:
    sequence: list[int] = [1, 2, 3]
    repeater_gen: Generator[Any, None, None] = repeater(sequence)
    for _ in range(10):
        print(next(repeater_gen))

if __name__ == "__main__":
    main()