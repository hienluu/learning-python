values: list[int] = [5,5,5,11,11,5, 20,30,30, 5, 11, 2,2,100]

def is_even(value: int) -> bool:
    return value % 2 == 0

filter_set: set[int] = {v*2 for v in values if v > 10 and is_even(v)}

print(filter_set)