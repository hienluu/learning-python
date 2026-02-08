from typing import Generator

def fib_generator() -> Generator[int, None, None]:
    a, b = 0,1
    while True:
        yield a # this make this a generator function
        # now comes the body of the generator function
        a, b = b, (a + b)

def main() -> None:
    fib_gen: Generator[int, None, None] = fib_generator()
    n: int = 5
    line_break: str = "=" * 20
    print(line_break)
    while True:
        user_input: str = input(f'Tap "Enter" to get the next {n} numbers, or "q" to quit: ')
        if user_input == "q":
            print("bye!")
            System.exit(0)
        else:
            for _ in range(n):
                print(f'{next(fib_gen)}')
            print(line_break)

if __name__ == "__main__":
    main()