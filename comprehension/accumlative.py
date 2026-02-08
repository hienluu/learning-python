from typing import Generator

def cumulative_sum() -> Generator[float, float, None]:
    total: float = 0.0
    while True:
        #new_value: float = yield total
        # yield retrieves the value from the generator
        total += yield total


def main() -> None:
    cumulative_gen: Generator[float, float, None] = cumulative_sum()
    next(cumulative_gen)

    while True:
        try:
            user_input: float = float(input('Enter a float value: '))
        except ValueError:
            print("Invalid input, please enter a float value")
            continue
        current_sum: float = cumulative_gen.send(user_input)
        print(f'current_sum: {current_sum}')
  
if __name__ == "__main__":
    main()