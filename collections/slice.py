"""
Slice object - used to slice sequences like lists, tuples, strings, etc.
- should learn more about this, it's a powerful tool.
"""
locker_numbers : list[int] = list(range(1, 15))
msg: str = "Hello, World!"

# reverse the list
print("==== reversing Using slide operator ====")
print(locker_numbers[::-1])
print(msg[::-1 ])


# using slice project
print("==== Using slice object by 1 step ====")
rev_by_1: slice = slice(None, None, -1)
print(locker_numbers[rev_by_1])
print(msg[rev_by_1])

# the last argument is the step
print("==== Using slice object by 2 step ====")
rev_by_2: slice = slice(None, None, -2)
print(locker_numbers[rev_by_2])
print(msg[rev_by_2])

# the first argument is the start
print("==== Using slice object starting from 10 ====")
rev_from_10: slice = slice(10, None, -1)
print(locker_numbers[rev_from_10])
print(msg[rev_from_10])

# the second argument is the end
print("==== Using slice object ending from 10 ====")
rev_to_10: slice = slice(None, 10, -1)
print(locker_numbers[rev_to_10])
print(msg[rev_to_10])