from typing import Generator


data: range = range(1, 10_000)

# generator comprehension starts with the result, then the for loop, 
# then the condition
# the Generator type is a special type that is used to generate a sequence of values    
# the first argument is the type of going to yield
# the second argument is the type goint to send to the generator
# the third argument is the type returned from the generator
squared: Generator[int, None, None] = (pow(x, 2) for x in data)

# squared is a generator object, so we can iterate over it
# we can use the next function to get the next value in the sequence
# the next function takes a generator object and returns the next value in the sequence
# generators are more efficient than lists because they generate values on the fly,
# rather than storing them in memory
print(squared)
print(next(squared))
print(next(squared))    
#for value in squared:
#    print(value)


# generator comprehension with a map function
squared2: Generator[int, None, None] = map(pow, data, [2 for _ in data])
#for value in squared2:
#    print(value)