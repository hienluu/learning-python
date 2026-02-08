from typing import Callable

def multiply_setup(a: int) -> Callable[[int], int]:
    def multiply(b: int) -> float:
        return a * b

    return multiply

double: Callable[[int], int] = multiply_setup(2)
triple: Callable[[int], int] = multiply_setup(3)

print("==== Double ====")
print(f"5 => {double(5)}")
print(f"10 => {double(10)}")

print("==== Triple ====")
print(f"6 => {triple(6)}")
print(f"10 => {triple(10)}")